from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^logout$', views.logout_view, name='logout_view'),
	url(r'^$', views.url_list, name='url_list'),
	url(r'^add', views.url_add, name='url_add'),
	url(r'^delete/(?P<id>[0-9]+)', views.url_delete, name='url_delete'),
	url(r'^api/$', views.api_list, name='api_list'),
	url(r'^api/add/$', views.api_add, name='api_add'),
	url(r'^api/id/(?P<id>[0-9]+)$', views.api_details, name='api_details'),
	url(r'^api/delete/(?P<id>[0-9]+)$', views.api_delete, name='api_delete'),
	url(r'^api/update/(?P<id>[0-9]+)$', views.api_update, name='api_update'),
]
