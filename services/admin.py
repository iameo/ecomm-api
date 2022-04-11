from django.contrib import admin
from .models import (Product, ProductItem, ProductOrder, ProductRating, ProductImage)

# Register your models here.


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','price','manufacturer','category')
    prepopulated_fields = {'slug': ("name",)}
    readonly_fields = ('ratings',)
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('user','product','ordered','quantity')

@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('user','reference_code','order_date','address', 'ordered')

@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ('user','product','rate', '__str__')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
        list_display = ('product', 'images')
