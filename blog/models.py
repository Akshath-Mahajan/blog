from django.db import models
from django.conf import settings

def upload_path_generator(instance, filename):
    return '/'.join(['profile', instance.title,str(instance.id), filename])

# Create your models here.
class BlogPost(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=2000)
    created_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(blank=True, null=True,upload_to=upload_path_generator)

class BlogLike(models.Model):
    blog=models.ForeignKey(BlogPost, on_delete=models.CASCADE,related_name='likes')
    like_author=models.CharField(max_length=200)

class BlogComment(models.Model):
    blog=models.ForeignKey(BlogPost, on_delete=models.CASCADE,related_name='comments')
    comment_author=models.CharField(max_length=200)
    comment_content=models.CharField(max_length=500)
    comment_date=models.DateTimeField(auto_now_add=True)

