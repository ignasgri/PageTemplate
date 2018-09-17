from django.conf.urls import url
from .views import *
from . import views


urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^(?P<id>\d+)/$', post_detail, name='post_detail'),
    url(r'^post/new/$', new_post, name='new_post'),
    url(r'^post/(?P<id>\d+)/edit$', edit_post, name='edit'),
]