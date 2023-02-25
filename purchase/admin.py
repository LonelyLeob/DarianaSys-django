from django.contrib import admin
from .models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'status']
    readonly_fields = ['id']

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request):
        return False