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
    pass

@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
