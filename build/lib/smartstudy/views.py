# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'home/main.html'
