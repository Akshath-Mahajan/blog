from django.contrib import admin
from .models import BlogComment, BlogLike, BlogPost
# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id','author','title','created_date', 'like_count', 'comment_count')
    list_filter = ('author', )
    search_fields = ('title', 'author__username')
    
class BlogLikeAdmin(admin.ModelAdmin):
    list_display = ('id','like_author','blog_title')
    def blog_title(self, obj):
        return obj.blog.title
    list_filter = ('like_author', )
    search_fields = ('blog__title', 'like_author__username')

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('id','comment_author','blog_title', 'comment')
    def blog_title(self, obj):
        return obj.blog.title
    def comment(self, obj):
        return obj.comment_content[:50]
    list_filter = ('comment_author', )
    search_fields = ('blog__title', 'comment_author__username')
  
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogLike, BlogLikeAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
