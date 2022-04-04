from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('product_ratings',)