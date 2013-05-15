# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from crew.models import Crew


class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['crew'] = Crew.objects.all().order_by('nick')
        context['products'] = [
            {'name': u'Robocca Poli',
             'icon': '/media/app/smartstudy.co.kr_robocarpoli_android_googlemarket.png',
             'category': 'animation',
             'description': u'Lorem ipsum.',
             'store_url': '#'},
            {'name': u'Best Kids Song & Stories',
             'icon': '/media/app/ssbooks.com_bodlebookiapfree.kr_android_googlemarket.png',
             'category': 'education',
             'description': u'대한민국 1등 어린이 교육 ∙ 놀이 앱',
             'store_url': '#'},
            {'name': u'매일무료만화:럭키짱',
             'icon': '/media/app/kimsungmo_icon.png',
             'category': 'book',
             'description': u'만화계의 레전드, 짤방의 원조.',
             'store_url': '#'},
            {'name': u'Tamago Monsters',
             'icon': '/media/app/tamago_icon.png',
             'category': 'game',
             'description': u'Lorem ipsum.',
             'store_url': '#'},
            {'name': u'Webtoon Camera',
             'icon': '/media/app/Classic_icon.png',
             'category': 'photography',
             'description': u'미국 교육 3위!!! 미국 어머니가 뽑은 한국 최고의 영어 교육앱!',
             'store_url': '#'},
        ]
        return context