from django.contrib import admin
from blog.models import Blog

from django.db import models
from django import forms

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'posted')
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        css = {
            "all": ("ckeditor/my_edit.css",)
        }
        js = ('ckeditor/ckeditor.js',)

admin.site.register(Blog, BlogAdmin)
