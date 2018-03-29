from django.conf.urls import url
from . import views
from rest_framework import routers
from aftorizate.viewsets.users import UserViewSet
# urlpatterns = [
#     url(r'^register', views.register, name ="register"),
#     url(r'^login', views.login_auth, name = "login"),
#     url(r'^logout', views.logout_auth, name = "logout")
# ]


router = routers.SimpleRouter()
router.register(r'^user/(?P<pk>\d+)', UserViewSet)
urlpatterns = router.urls
