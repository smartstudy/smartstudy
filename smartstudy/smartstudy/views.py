# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = 'home/main.html'


def privacy(request):
    return render(request, 'privacy.html')
