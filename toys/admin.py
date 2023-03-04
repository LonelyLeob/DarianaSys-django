from django.contrib import admin
from .models import Material, Toy, ToyImage

@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ['title',]
    readonly_fields = ['pk',]
    exclude = ['pk',]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['title']
    readonly_fields = ['pk',]
    exclude = ['pk',]


@admin.register(ToyImage)
class ToyImageAdmin(admin.ModelAdmin):
    list_display = ['title',]
    exclude = ['pk',]
