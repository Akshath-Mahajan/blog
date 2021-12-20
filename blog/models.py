from django.db import models
from django.conf import settings

# Create your models here.

class BlogPost(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=2000)
    created_date=models.DateTimeField(auto_now_add=True)
    