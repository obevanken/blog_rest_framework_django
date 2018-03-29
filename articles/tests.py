from django.test import TestCase
from .models import Articles

class ArticlesTestCase(TestCase):
    def create(self):
        Articles.objects.create(title = "Test", body = "TestBody")
