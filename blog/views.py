from django.shortcuts import render
from django.views import ListView,DetailView
from .models import BlogPost,BlogComment,BlogLike

# Create your views here.
class HomeView(ListView):
    model = BlogPost
    template_name = ''

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = ''

class GetComments(DetailView):
    model=BlogComment
    template_name=''

class GetLikes(DetailView):
    model=BlogLike
    template_name=''