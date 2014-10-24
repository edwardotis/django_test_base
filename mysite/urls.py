# coding=utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
from mysite import settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
                       (r'^accounts/', include('django.contrib.auth.urls')),
                       # use simple for development, and default for prod
                       (r'^accounts/', include('registration.backends.simple.urls')),
                       (r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^addressbook/', include('addressbook.urls', namespace="addressbook")),
)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)), )