from django.conf.urls import url

from . import views

app_name = 'venues'
urlpatterns = [
    url(r'^test', views.test, name='test'),
    url(r'^home', views.home, name='home'),
    url(r'^venue_list', views.view_venues, name='venue_list'),
    url(r'^venue_info', views.venue_more_info, name='venue_info'),
]