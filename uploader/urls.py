from django.conf.urls import patterns, url

urlpatterns = patterns(
    'uploader.views',
    url(r'^list/$', 'list', name='list'),
)
