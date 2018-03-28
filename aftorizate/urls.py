from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register', views.register, name ="register"),
    url(r'^login', views.login_auth, name = "login"),
    url(r'^logout', views.logout_auth, name = "logout")
]
