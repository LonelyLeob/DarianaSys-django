from django.contrib import admin
from .models import Purchase, PurchaseItem

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'status']
    readonly_fields = ['pk', 'user_id']

    def has_add_permission(self, _):
        return False
    
    def has_delete_permission(self, _):
        return False
    
@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'toy_id', 'amount']
    readonly_fields = ['pk', 'toy_id', 'amount']

    def has_add_permission(self, _):
        return False
    
    def has_delete_permission(self, _):
        return False