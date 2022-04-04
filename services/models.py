from unicodedata import category
from django.db import models

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

from utils import TimeStampMixin


class Product(TimeStampMixin):
    """
    This is the Product Model which is populated by the Seller
    """
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.CharField(max_length=500)
    quantity = models.IntegerField(default=1, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    ratings = models.FloatField(default=0.0)
    shipping = models.CharField(max_length=200)
    details = models.TextField(max_length=5000)
    category = models.CharField(max_length=50, default='others')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.description[:20]} (Seller: {self.products})"

    class Meta:
        db_table = 'product_db'


class ProductItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"ProductItem({self.quantity} x {self.product.name})"

class ProductOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductItem)
    reference_code = models.CharField(max_length=20, blank=True, null=True)
    order_date = models.DateTimeField()
    address = models.CharField(max_length=500)
    ordered = models.BooleanField(default=False)


class ProductRating(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return f'{self.user.full_name} rated Product({self.product.name}) {self.rate} stars'
