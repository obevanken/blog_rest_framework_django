from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField("Заголовок", max_length = 120)
    body = models.TextField("Текст статьи")
    date = models.DateTimeField("Дата добавления", auto_now_add = True)
    update = models.DateTimeField("Дата обновления", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True, related_name='user')

    def __str__(self):
        return self.title
