from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


def upload_path_generator(instance, filename):
    return '/'.join(['blog', str(instance.pk), filename])

# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to=upload_path_generator)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

class BlogLike(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='likes')
    like_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

@receiver(post_save, sender=BlogLike)
def create_profile(sender, instance, **kwargs):
    update_blog = instance.blog
    update_blog.like_count += 1
    update_blog.save()

@receiver(post_delete, sender=BlogLike)
def create_profile(sender, instance, **kwargs):
    update_blog = instance.blog
    update_blog.like_count -= 1
    update_blog.save()

class BlogComment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=BlogComment)
def create_profile(sender, instance, **kwargs):
    update_blog = instance.blog
    update_blog.comment_count += 1
    update_blog.save()

@receiver(post_delete, sender=BlogComment)
def create_profile(sender, instance, **kwargs):
    update_blog = instance.blog
    update_blog.comment_count -= 1
    update_blog.save()
