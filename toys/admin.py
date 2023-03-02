from django.contrib import admin
from .models import Material, Toy, ToyImage

@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    readonly_fields = ['pk',]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']
    readonly_fields = ['pk',]

@admin.register(ToyImage)
class ToyImageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'url_path']
    