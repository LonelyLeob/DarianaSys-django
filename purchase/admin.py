from django.contrib import admin
from .models import Purchase, PurchaseItem

#temporarily blocked constraints

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'status']
    # readonly_fields = ['pk', 'user']
    exclude = ['pk',]

    # def has_add_permission(self, *_):
    #     return False
    
    def has_delete_permission(self, *_):
        return False
    
@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'toy', 'quantity']
    # readonly_fields = ['pk', 'toy', 'quantity']
    exclude = ['pk',]

    # def has_add_permission(self, *_):
    #     return False
    
    def has_delete_permission(self, *_):
        return False