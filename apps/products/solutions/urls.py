from django.conf.urls import url, include, patterns
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='solutions'),
]
