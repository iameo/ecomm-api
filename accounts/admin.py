from django.contrib import admin
from .models import ProductBuyer, ProductManager, CustomUser, SellerRating

# Register your models here.

@admin.register(ProductBuyer)
class BuyerAdmin(admin.ModelAdmin):
    readonly_fields = ('purchased_counts',)
    date_hierarchy = 'acc_type__joined'

@admin.register(ProductManager)
class SellerAdmin(admin.ModelAdmin):
    readonly_fields = ('availability', 'ratings', 'last_service')
    date_hierarchy = 'acc_type__joined'

@admin.register(SellerRating)
class SellerRatingAdmin(admin.ModelAdmin):
    # readonly_fields = ('rate',)
    pass

admin.site.register(CustomUser)

