'''
Created on Apr 3, 2016

@author: jannainm
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /information/
    url(r'^$', views.index, name='index'), # index is name of function in views.py
    # ex: /information/5
    url(r'^(?P<incidentName>[0-9]+)/$', views.detail, name='detail'), # detail is name of function in views.py
]
