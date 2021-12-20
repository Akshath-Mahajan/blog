from django.db import models
from django.conf import settings

def upload_path_generator(instance, filename):
    return '/'.join(['profile', instance.user.username, filename])
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_path_generator)