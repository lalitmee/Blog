from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    #url(r'^posts/$', "<appname>.views.<function_name>"),
    url(r'^$', "blog.views.post_list", name='list'),
    url(r'^create/$', "blog.views.post_create"),
    url(r'^(?P<id>\d+)/$', "blog.views.post_detail", name='detail'),
    url(r'^(?P<id>\d+)/edit/$', "blog.views.post_update", name='update'),
    url(r'^^(?P<id>\d+)/delete/$', "blog.views.post_delete"),

]
