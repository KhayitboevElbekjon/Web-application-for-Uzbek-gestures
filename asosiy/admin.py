from django.contrib import admin
from .models import *
# admin.site.register(Bolim)
# admin.site.register(Sozlar)

@admin.register(Bolim)
class BolimAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    list_filter = ('nom',)
    search_fields = ('nom',)
@admin.register(Sozlar)
class SozlarAdmin(admin.ModelAdmin):
    list_display = ('bolim_fk','nom')
    list_display_links = ('nom',)
    list_filter = ('bolim_fk',)
    search_fields = ('nom',)
    list_per_page = 8