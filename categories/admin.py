from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'catname')
    list_display_links = ('id', 'catname')

admin.site.register(Category, CategoryAdmin)
