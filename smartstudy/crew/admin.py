# -*- coding: utf-8 -*-
from django.contrib import admin
from crew.models import Crew


def picture(self):
    return '<a href="%s"><img src="%s" width="50" /></a>' % (self.id, self.picture.url)


picture.short_description = u'사진'
picture.allow_tags = True


class Admin_Crew(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/admin.css",)
        }

    list_display = ('id', picture, 'name', 'nick', 'email', 'twitter', 'facebook', 'home',)
    list_editable = ('email', 'twitter', 'facebook', 'home',)
    list_display_links = ('id',)
    search_fields = ['uid', 'nick', 'comment', ]
    ordering = ('-id',)


admin.site.register(Crew, Admin_Crew)
