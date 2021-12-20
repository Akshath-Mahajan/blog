from django.urls import path
from .views_class import CreateBlog, UpdateBlog, DeleteBlog
urlpatterns = [
    path('create/', CreateBlog.as_view(), name="create_blog"),
    path('update/<int:pk>/', UpdateBlog.as_view(), name="update_blog"),
    path('delete/<int:pk>/', DeleteBlog.as_view(), name="dreate_blog"),
]