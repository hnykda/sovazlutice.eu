from django.contrib import admin
from ways.models import Way
from django.db import models
from django import forms

class WayAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', )

    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        css = {
            "all": ("ckeditor/my_edit.css",)
        }
        js = ('ckeditor/ckeditor.js',)

admin.site.register(Way, WayAdmin)
