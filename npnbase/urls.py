from django.conf.urls import url
from npnbase import views

urlpatterns = [
    url(r'^names/$', views.names_list),
    url(r'^names/(?P<month>[1-12])/$', views.names_detail),
    url(r'^names/(?P<month>[1-12])/(?P<group>\w+)/$', views.names_detail),
    url(r'^names')
]
