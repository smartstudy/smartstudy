# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
    template_name = 'home/main.html'
<<<<<<< HEAD


def privacy(request):
    return render(request, 'privacy.html')
=======
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        context['crew'] = {}
        return context
>>>>>>> crew 초안만듬
