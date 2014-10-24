# coding=utf-8
__author__ = 'edwardotis'

from django.conf.urls import patterns, url

from addressbook import views

urlpatterns = patterns(
    '',
    # For static template pages
    url(r'^$', views.template_view, kwargs={'template_name': 'addressbook/index.html'}, name='home'),

    # school views
    url(r'^school/$', views.school_list, name='school_list'),
    url(r'^school/new', views.create_school, name='create_school'),
    url(r'^school/(?P<school_id>\d+)/edit$', views.update_school, name='update_school'),
    url(r'^school/(?P<school_id>\d+)/delete$', views.delete_school, name='delete_school'),
    # pk is a magic django param that looks up the object in the db by pk
    url(r'^school/(?P<pk>\d+)/$', views.school_detail, name='school_detail'),

)
