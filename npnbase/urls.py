from django.conf.urls import url
from npnbase import views

urlpatterns = [
    url(r'^names/$', views.names_list),
    url(r'^names/(?P<pk>[0-9]+)/$', views.names_detail),
]
