from django.contrib import admin
from .models import ProductBuyer, ProductManager, CustomUser

# Register your models here.

@admin.register(ProductBuyer)
class BuyerAdmin(admin.ModelAdmin):
    readonly_fields = ('purchased_counts',)
    date_hierarchy = 'acc_type__joined'

@admin.register(ProductManager)
class SellerAdmin(admin.ModelAdmin):
    readonly_fields = ('availability', 'ratings', 'last_service', 'rendered_services')
    date_hierarchy = 'acc_type__joined'

admin.site.register(CustomUser)