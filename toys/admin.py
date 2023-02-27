from django.contrib import admin
from .models import Material, Toy

@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    readonly_fields = ['pk',]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    readonly_fields = ['pk',]