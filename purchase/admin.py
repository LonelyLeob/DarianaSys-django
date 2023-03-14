from django.contrib import admin
from .models import Purchase, PurchaseItem, CanceledPurchase
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.shortcuts import redirect

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'status', 'view_items']
    readonly_fields = ['pk', 'user', 'items']
    empty_value_display = 'Не назначено'

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
        if len(formatter) < 1:
            return "Произошла ошибка, обратитесь к системному администратору"
        return format_html(" , ".join(formatter))
    view_items.short_description = "Предметы"

    def has_add_permission(self, *_):
        return False
    
    # cancel purchase in admin panel
    def delete_model(self, _, obj):
        cancel_pur = CanceledPurchase.objects.create(user=obj.user, created_at=obj.created_at)
        cancel_pur.items.set(obj.items.all())
        obj.delete()
        return redirect(reverse("admin:purchase_canceledpurchase_changelist"))
    

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
    list_display = ['pk', 'user', 'view_items']
    readonly_fields = ['pk', 'user']

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
        if len(formatter) < 1:
            return "Произошла ошибка, обратитесь к системному администратору"
        return format_html(" , ".join(formatter))
    view_items.short_description = "Предметы"

    def has_add_permission(self, *_):
        return False
    
    def has_delete_permission(self, *_):
        return False