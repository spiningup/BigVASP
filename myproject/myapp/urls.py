from django.conf.urls import patterns, url

urlpatterns = patterns('myapp.views',
    url(r'^list/$', 'list', name='list'),
)
