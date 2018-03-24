from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.posts, name ="posts"),
    url(r'^create/', views.post, name = "post"),
]
