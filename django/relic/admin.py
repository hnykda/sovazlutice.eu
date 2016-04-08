from django.contrib import admin
from relic.models import Relic

from django.db import models
from django import forms

class RelicAdmin(admin.ModelAdmin):
#    exclude = ['slug']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'series_num', 'posted', 'type_of_r', 'w_ssr', 'w_kc', 'w_czp')

    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        css = {
            "all": ("ckeditor/my_edit.css",)
        }
        js = ('ckeditor/ckeditor.js',)

admin.site.register(Relic, RelicAdmin)
