from django.conf.urls import url
from . import views
from articles.viewsets.post import ArticlesViewSet
# urlpatterns = [
#     url(r'^$', views.posts, name ="posts"),
#     url(r'^create/$', views.create, name = "create"),
#     url(r'^post/(?P<pk>\d+)$', views.post, name = "post")
# ]

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'', ArticlesViewSet)
urlpatterns = router.urls
