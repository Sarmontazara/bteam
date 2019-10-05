from django.contrib import admin
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'index.html', views.index, name='index'),
    re_path(r'blog.html', views.blog, name='blog'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'thanks.html', views.thanks, name='thanks'),
    re_path(r'yandex_2ce42828c2811ce8.html', views.yandexver, name='yandexver'),
    re_path(r'^links1059627.html', views.links, name='links'),
    re_path(r'^policy.html', views.policy, name='policy'),
    re_path(r'^seosan-verification-f45fecc59a2f45da.html', views.seosan, name='seosan'),
]