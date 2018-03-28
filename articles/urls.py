from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts, name ="posts"),
    url(r'^create/$', views.create, name = "create"),
    url(r'^post/(?P<pk>\d+)$', views.post, name = "post")
]
