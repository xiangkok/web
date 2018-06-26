#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "longyucen"
# Date: 2018/6/20

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('model', views.model, name='model'),
    path('tag', views.tag, name='tag'),
    path('platform', views.platform, name='platform'),
    path('search', views.search, name='search')
]
