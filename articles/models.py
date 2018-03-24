from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 120)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True, auto_now = False)

    def __str__(self):
        return self.title
