from django.contrib import admin
from .models import User, TokenStorage

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    readonly_fields = ['username', 'first_name', 'age', 'password']
    exclude = ['pk',]

    def has_add_permission(self, *_):
        return False

@admin.register(TokenStorage)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['user']
    readonly_fields = ['pk', 'user_id', 'refresh']
    exclude = ['pk',]

    def has_add_permission(self, *_):
        return False
    
    def has_delete_permission(self, *_):
        return False