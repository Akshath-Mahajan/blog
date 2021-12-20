from django.shortcuts import render
from django.views import ListView,DetailView
from .models import BlogPost,BlogComment,BlogLike

# Create your views here.
class HomeView(ListView):
    model = BlogPost
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'posts': BlogPost.objects.filter(author=request.user)})

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'post.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'post': BlogPost.objects.get(id=self.kwargs['pk']), 'comments': BlogPost.comments.get(id=self.kwargs['pk']), 'likes': BlogPost.likes.get(id=self.kwargs['pk'])})


class GetComments(DetailView):
    model=BlogComment
    template_name=''

class GetLikes(DetailView):
    model=BlogLike
    template_name=''
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'likes': BlogLike.objects.filter(blog__id=self.kwargs['pk'])})
    def post(self, request, *args, **kwargs):
        pass