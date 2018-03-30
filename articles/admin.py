from django.contrib import admin
from .models import *

class ArticleTes(admin.ModelAdmin):
    list_display = [field.name for field in Articles._meta.fields]
    list_filter = ['title',]
    exclude = ["user",]
    class Meta:
        model = Articles

admin.site.register(Articles, ArticleTes)

# Register your models here.
