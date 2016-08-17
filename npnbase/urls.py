from django.conf.urls import url
from npnbase import views

urlpatterns = [
    url(r'^names/$', views.names_list),
    url(r'^names/(?P<month>[0-12])/(?P<sex>[0-2])/(?P<group>\w+)/$', views.names_detail),
]
