from django.contrib import admin
from .models import User, TokenStorage

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    readonly_fields = ['username', 'first_name', 'age', 'password']
    def has_add_permission(self, request):
        return False

@admin.register(TokenStorage)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id']
    readonly_fields = ['id', 'user_id', 'refresh']

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request):
        return False