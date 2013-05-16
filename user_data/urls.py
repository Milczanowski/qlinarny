from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',
	url(r'^(?P<user_name>\S+)/$', 'user_data.views.index'),

)