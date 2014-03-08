from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()views
from energysaverapp import views
urlpatterns = patterns('',
    url(r'^index/', views.index, name='index'),
    url(r'^approach/', views.approach, name='index'),
    url(r'^social/', views.socialView, name='social'),
    url(r'^personal/', views.personalView, name='social'),
    url(r'^infograp/', views.infoGraphView, name='social'),
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
