from django.conf.urls import url
from npnbase import views

urlpatterns = [
    url(r'^names/$', views.names_list),
    url(r'^names/(?P<month>\d+)/(?P<sex>\d+)/(?P<group>\w+)/$', views.names_detail),
    url(r'^names/new/$', views.names_new, name='names_new'),
]
