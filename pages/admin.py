from django import forms
import django
from pages.models import Teams
from django.contrib import admin
from .models import Teams
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))

    thumnail.short_description=('photos')

    list_display=('id','thumnail','first_name','last_name', 'desgin', 'created_date')
    list_display_links=('id','first_name', 'last_name')
    search_fields=('first_name','last_name', 'desgin')
    list_filter=('first_name','last_name', 'desgin')


admin.site.register(Teams, TeamAdmin)