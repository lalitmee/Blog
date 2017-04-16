from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    #url(r'^posts/$', "<appname>.views.<function_name>"),
    url(r'^$', "blog.views.post_list"),
    url(r'^create/$', "blog.views.post_create"),
    url(r'^detail/$', "blog.views.post_detail"),
    url(r'^update/$', "blog.views.post_update"),
    url(r'^delete/$', "blog.views.post_delete"),

]
