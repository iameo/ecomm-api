from django.contrib import admin
from .models import (Product, ProductItem, ProductOrder)

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('ratings',)

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    pass