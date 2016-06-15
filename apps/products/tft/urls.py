from django.conf.urls import url

from . import views

app_name = 'tft'
urlpatterns = [
    url(r'^$', views.IndexView, name='tft_list'),
    url(r'^all/$', views.IndexViewAll.as_view(), name='tft_list_all'),
    url(r'^data/$', views.IndexViewAll.as_view(), name='tft_list_all'),
    url(r'^production/$', views.IndexViewProd.as_view(), name='tft_list_prod'),
    url(r'^obsolete/$', views.IndexViewObsolete.as_view(), name='tft_list_obsolete'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='tft_detail'),
]