#!/Users/alextan/GitHub/demos/django_demos/venv python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 14:22
# @Author  : urls.py 
# @Site    : 
# @File    : urls.py.py
# @Software: PyCharm

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index')
]