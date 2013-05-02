# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.shortcuts import render
from crew.models import Crew


class HomeView(TemplateView):
    template_name = 'home/main.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['crew'] = Crew.objects.all() 
        return context

def privacy(request):
    return render(request, 'privacy.html')