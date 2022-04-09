from tabnanny import verbose
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, User
from django.core.mail import send_mail
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from accounts.managers import CustomUserManager

from django.urls import reverse

from services.models import Product


_phone_regex = RegexValidator(
        regex=r"\+?1?\d{10,14}$",
        message="Phony"
    )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    CustomUser is the abstract base user class for every other user in the API (customer, seller, etc)
    """
    email = models.EmailField(max_length=300, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, null=True, blank=True, validators=[_phone_regex])
    display_photo = models.ImageField(upload_to='images/users/', default='avatar-img.png')
    location = models.CharField(max_length=100, default="Nigeria")
    date_of_birth = models.DateField('date_of_birth', null=False, blank=False)
    joined = models.DateTimeField('date_joined', default=timezone.now)

    is_productManager = models.BooleanField(default=False)
    is_productBuyer = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    
    REQUIRE_FIELDS = ('email', 'first_name', 'last_name', 'phone', 'location', 'dob')


    USERNAME_FIELD = 'email'

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return f'{self.email}'

    objects = CustomUserManager()


class ProductBuyer(models.Model):
    """
    The ProductBuyer model represents the customer
    """

    acc_type = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name='customer')
    purchased_counts = models.IntegerField(default=0)

    # def get_absolute_url(self): 
    #     return reverse('myprofile', args=[int(self.acc_type.id)])

    def __str__(self):
        return f'{self.acc_type.full_name}'
    
    class Meta:
        verbose_name = 'Customer'




class ProductManager(models.Model):
    """
    This model handles the seller of a product
    """
    acc_type = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, related_name="product_owner")

    ratings = models.FloatField(default=0.0)
    last_service = models.DateField('last_service_time', blank=True, null=True)
    availability = models.BooleanField(default=False)
    rendered_services = models.ManyToManyField(ProductBuyer, blank=True)
    products = models.ManyToManyField(Product, blank=True, related_name='seller')

    @property
    def average_ratings(self):
        avg_star = self.rating_set.all()
        if avg_star:
            return avg_star.aggregate(models.Avg('ratings'))['rate__avg']
        return 0

    @property
    def rate_count(self):
        return self.rating_set.all().count()

    def is_working(self):
        if self.availability:
            self.last_service = models.DateTimeField(default=timezone.now)


    @property
    def done_job(self):
        if self.rendered_services:
            return self.rendered_services.all()
        else:
            return None, 'ff'
    
    def get_absolute_url(self): 
        return reverse('myprofile', args=[int(self.acc_type.id)])

    def __str__(self):
        return f'{self.acc_type.full_name} (availability: {self.availability} | ratings: {self.ratings})'
    
    class Meta:
        ordering = ['-acc_type__joined']
        verbose_name = "Seller"


class SellerRating(models.Model):
    seller = models.ForeignKey(ProductManager, on_delete=models.CASCADE)
    customer = models.ForeignKey(ProductBuyer, on_delete=models.CASCADE)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return f'{self.customer.acc_type.full_name} rated Seller({self.seller.acc_type.full_name}) {self.rate} stars'

    class Meta:
        verbose_name = "Seller's Rating"



def user_build(user_type, instance):
    instance_ = user_type.objects.create(acc_type=instance)
    if hasattr(instance_, 'availability'):
        instance_.availability = True
    instance_.save()
    return instance_

def user_type_post_save(sender, instance, created, *args, **kwargs):
    if created:
        if instance.is_productManager:
            user_build(ProductManager, instance)
        if instance.is_productBuyer:
            user_build(ProductBuyer, instance)
models.signals.post_save.connect(user_type_post_save, sender=CustomUser)

