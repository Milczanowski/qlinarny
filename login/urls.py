from django.conf.urls import patterns, include, url
from django.conf import settings


urlpatterns = patterns('',	
	url(r'^zarejestruj/$', 'login.views.zarejestruj'),  	
	url(r'^(?P<user_name>\S+)/(?P<user_id>\d+)/aktywuj/$', 'login.views.aktywuj'),
	url(r'^wyloguj/$', 'login.views.wyloguj'),  
	url(r'^profil/$', 'login.views.profile'),  
	url(r'^stworzone/$', 'login.views.stworzone'),

)