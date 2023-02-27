from django.contrib import admin
from .models import Purchase, PurchaseItem

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    readonly_fields = ['id']

    def has_add_permission(self, _):
        return False
    
    def has_delete_permission(self, _):
        return False
    
@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'toy_id', 'amount']
    readonly_fields = ['id', 'toy_id', 'amount']

    def has_add_permission(self, _):
        return False
    
    def has_delete_permission(self, _):
        return False