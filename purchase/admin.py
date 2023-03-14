from django.contrib import admin
from .models import Purchase, PurchaseItem, CanceledPurchase
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'status', 'view_items']
    readonly_fields = ['pk', 'user', 'items']

    def view_items(self, obj):
        formatter = []
        url = ""
        for item in obj.items.all():
            url = (
                reverse("admin:purchase_purchaseitem_changelist") 
                + "?"
                + urlencode({"id": f"{item.id}"})
            )
            formatter.append(f"<a href={url}>{item}</a>")
        return format_html(" , ".join(formatter))

    def has_add_permission(self, *_):
        return False
    
    def has_delete_permission(self, *_):
        return False
    
@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['toy', 'quantity']
    readonly_fields = ['pk', 'toy', 'quantity']

    def has_add_permission(self, *_):
        return False
    
    def has_delete_permission(self, *_):
        return False
    
@admin.register(CanceledPurchase)
class CanceledPurchaseAdmin(admin.ModelAdmin):
    list_display = ['pk']
    readonly_fields = ['pk', 'user']

    def has_add_permission(self, *_):
        return False
    
    def has_delete_permission(self, *_):
        return False