# ecoding=utf-8
# Author: 翁彦彬 | Sven_Weng
# Email : sven_weng@wengyb.com
# Web   : http://wybblog.applinzi.com

from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.index),
	url(r'^getlog/', views.get_log),
	url(r'^getapilog/', views.get_api_log),
]
