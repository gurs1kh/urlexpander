from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.url_list, name='url_list'),
	url(r'^add', views.url_add, name='url_add'),
	url(r'^delete/(?P<id>[0-9]+)', views.url_delete, name='url_delete'),
]
