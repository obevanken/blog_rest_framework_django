from rest_framework import serializers
from django.contrib.auth.models import User
from articles.models import Articles
from articles.serializers import ArticlesSerializer


class UserSerializer(serializers.ModelSerializer):
    articles = ArticlesSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
