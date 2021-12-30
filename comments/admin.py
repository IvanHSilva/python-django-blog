from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'post', 'comdate', 'published')
    list_editable = ('published', )
    list_display_links = ('id', 'name', 'email')

admin.site.register(Comment, CommentAdmin)
