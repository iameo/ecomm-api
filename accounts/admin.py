from django.contrib import admin
from .models import ProductBuyer, ProductManager, CustomUser, SellerRating

# Register your models here.

@admin.register(ProductBuyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('acc_type', 'name', 'purchased_counts', 'phone')
    readonly_fields = ('purchased_counts',)
    date_hierarchy = 'acc_type__joined'
    
    @admin.display(empty_value='')
    def name(self, obj):
        return obj.acc_type.full_name
    
    @admin.display(empty_value='')
    def phone(self, obj):
        return obj.acc_type.phone
    

@admin.register(ProductManager)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('acc_type', 'name', 'ratings','availability','last_service', 'phone')
    readonly_fields = ('availability', 'ratings', 'last_service')
    date_hierarchy = 'acc_type__joined'

    @admin.display(empty_value='')
    def phone(self, obj):
        return obj.acc_type.phone
        
    @admin.display(empty_value='')
    def name(self, obj):
        return obj.acc_type.full_name

@admin.register(SellerRating)
class SellerRatingAdmin(admin.ModelAdmin):
    # readonly_fields = ('rate',)
    pass

admin.site.register(CustomUser)

