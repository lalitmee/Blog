from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    #url(r'^posts/$', "<appname>.views.<function_name>"),
    url(r'^$', "blog.views.post_home"),

]
