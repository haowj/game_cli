#!/usr/bin/env python3
# -*- coding: utf8 -*-
__author__ = 'wjhao'
from django.urls import path
from client.views import IntegralSelect
app_name = 'client'
urlpatterns = [
    path('', IntegralSelect.as_view()),#cvb方式
]
