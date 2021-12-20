from django.urls import path
from .views_class import CreateBlog, UpdateBlog, DeleteBlog
from .views import CreateComment, CreateLike, HomeView, BlogDetailView
urlpatterns = [
    path('', HomeView.as_view()),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', CreateBlog.as_view(), name="create_blog"),
    path('update/<int:pk>/', UpdateBlog.as_view(), name="update_blog"),
    path('delete/<int:pk>/', DeleteBlog.as_view(), name="dreate_blog"),

    # API:
    path('<int:pk>/like/', CreateLike.as_view(), name="create_like"),
    path('<int:pk>/comment/', CreateComment.as_view(), name="create_comment"),
]