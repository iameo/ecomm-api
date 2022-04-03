from django.db import models

from accounts.models import ProductManager

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_image = models.ImageField()
    product_description = models.CharField(max_length=500)
    product_quantity = models.IntegerField(default=1, blank=False)
    product_ratings = models.FloatField(default=0.0)
    product_shipping = models.CharField(max_length=200)
    product_details = models.TextField(max_length=5000)
    seller = models.ForeignKey(ProductManager, blank=False, null=False, related_name='seller_info', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name} - {self.seller} - {self.product_description[:20]}"
