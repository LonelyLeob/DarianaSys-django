from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment']
    readonly_fields = ['id', 'toy_id', 'commenter_id', 'comment']
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request):
        return False