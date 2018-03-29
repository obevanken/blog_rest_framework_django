from articles.models import Articles
from articles.serializers import ArticlesSerializer
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ArticlesViewSet(mixins.CreateModelMixin, GenericViewSet, mixins.ListModelMixin):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ArticlesSerializer(queryset, many=True)
        return Response(serializer.data)
