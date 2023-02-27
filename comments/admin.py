from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'comment']
    readonly_fields = ['pk', 'toy_id', 'commenter_id', 'comment']
    
    def has_add_permission(self, _):
        return False
    
    def has_delete_permission(self, _):
        return False