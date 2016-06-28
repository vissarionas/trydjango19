from django.conf.urls import url
from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
    url(r'^$', post_list , name='posts'),
    url(r'^create/$', post_create),
    url(r'^(?P<post_id>\d+)/$', post_detail, name = 'detail'),
    url(r'^(?P<post_id>\d+)/update/$', post_update, name = 'update'),
    url(r'^(?P<post_id>\d+)/delete/$', post_delete , name = 'delete'),
]
