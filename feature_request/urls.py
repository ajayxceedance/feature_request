"""feature_request URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""

from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
"""  Define base url for our project """
urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='list_showing.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('create_request.urls')),
]


