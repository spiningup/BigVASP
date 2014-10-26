# -*- coding: utf-8 -*-
from django.conf.urls import *

urlpatterns = patterns(
    'authsys.views',
    url(r'^$', 'index', name='index'),
    url(r'^signin/$', 'signin', name='signin'),
    url(r'^signout/$', 'signout', name='signout'),
)
