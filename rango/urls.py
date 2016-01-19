from django.conf.urls import patterns, url
from rango import views
#rango = bares

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^login/$', views.userlogin, name='login'),
        url(r'^registro/$', views.registro, name='registro'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^category/$', views.category, name='category'), # NEW MAPPING!
        url(r'^categorys/(?P<category_name_slug>[\w\-]+)/$', views.category, name='categorys'),
        url(r'^restringido/', views.restricted, name='restricted'),
        )