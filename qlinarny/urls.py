from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',	
    url(r'^$', 'django.contrib.auth.views.login'), 
    url(r'^accounts/', include('login.urls')),      
    url(r'^user/' , include('user_data.urls')),
    url(r'^przepis/', include('przepis.urls')),   
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/$', 'qlinarny.views.profile'),    
)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),    
) + urlpatterns