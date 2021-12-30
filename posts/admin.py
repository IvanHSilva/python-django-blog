from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'author', 'postdate', 'catpost', 'published')
    list_editable = ('published', )
    list_display_links = ('id', 'title')
    summernote_fields = ('content', )

admin.site.register(Post, PostAdmin)
