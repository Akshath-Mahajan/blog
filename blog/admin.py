from django.contrib import admin
from .models import BlogComment, BlogLike, BlogPost
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogLike)
admin.site.register(BlogComment)
