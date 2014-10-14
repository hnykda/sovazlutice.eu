from django.contrib import admin
from relic.models import Relic
from django_summernote.admin import SummernoteModelAdmin

class RelicAdmin(SummernoteModelAdmin):
#    exclude = ['slug']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'series_num', 'posted', 'type_of_r', 'w_ssr', 'w_kc', 'w_czp')

admin.site.register(Relic, RelicAdmin)
