# -*- coding: utf-8 -*-
from django.contrib import admin
from crew.models import Crew

class Admin_Crew(admin.ModelAdmin):
    list_display = ('id', 'nick', 'picture', 'comment',)
    list_display_links = ('id',)
    search_fields = ['nick', 'comment', ]
    ordering = ('-id',)

admin.site.register(Crew, Admin_Crew)