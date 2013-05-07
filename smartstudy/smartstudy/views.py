# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from crew.models import Crew


class HomeView(TemplateView):
    template_name = 'home/main.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['crew'] = Crew.objects.all().order_by('nick')
        context['products'] = [
            {'name': u'퐁! 인기동요∙동화',
             'icon': '/media/app/ssbooks.com_bodlebookiapfree.kr_android_googlemarket.png',
             'description': u'대한민국 1등 어린이 교육 ∙ 놀이 앱',
             'store_url': '#'},
            {'name': u'인기육아잡지: 베이비',
             'icon': '/media/app/ssbooks.com_colorbook.kr_android_googlemarket.png',
             'description': u'즐거운 육아! 행복한 엄마! Babee(베이비)!',
             'store_url': '#'},
            {'name': u'매일무료만화:럭키짱',
             'icon': '/media/app/kimsungmo_icon.png',
             'description': u'만화계의 레전드, 짤방의 원조.',
             'store_url': '#'},
            {'name': u'진짜 어린이집 영단어',
             'icon': '/media/app/Classic_icon.png',
             'description': u'미국 교육 3위!!! 미국 어머니가 뽑은 한국 최고의 영어 교육앱!',
             'store_url': '#'},
            {'name': u'로보카 폴리',
             'icon': '/media/app/smartstudy.co.kr_robocarpoli_android_googlemarket.png',
             'description': u'Lorem ipsum.',
             'store_url': '#'},
            {'name': u'타마고 몬스터즈',
             'icon': '/media/app/tamago_icon.png',
             'description': u'Lorem ipsum.',
             'store_url': '#'},
        ]
        context['products'] += context['products']
        return context