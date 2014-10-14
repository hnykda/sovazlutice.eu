from django.contrib import admin
from ways.models import Way
from django_summernote.admin import SummernoteModelAdmin

class WayAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', )

admin.site.register(Way, WayAdmin)
