from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    readonly_fields = ['username', 'first_name', 'age', 'password']
    exclude = ['pk',]

    def has_add_permission(self, *_):
        return False