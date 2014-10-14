from django.contrib import admin
from blog.models import Blog
from django_summernote.admin import SummernoteModelAdmin

class BlogAdmin(SummernoteModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'posted')

admin.site.register(Blog, BlogAdmin)
