# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from . import forms


urlpatterns = patterns('',
    url(r'^$', 'index', name='index'),
    # Buitlin Login Agent
    url(r'^login/$', 'django.contrib.auth.views.login', {
                            'template_name': 'authsys/signin.html', 
                            'authentication_form': forms.AuthenticationForm
                    },
                    name='signin'),

    url(r'^logout/$', 'django.contrib.auth.views.logout',{
                            'next_page':'/'
                    },
                    name='signout'),
)
