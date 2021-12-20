from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView,DetailView, CreateView, UpdateView
from .models import BlogPost,BlogComment,BlogLike
from django.views import View
# Create your views here.
class HomeView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'posts': BlogPost.objects.all()})

class HomeView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'posts': BlogPost.objects.all()})

class UserView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'posts': BlogPost.objects.filter(author=request.user)})
    
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post.html'
    def get(self, request, *args, **kwargs):
        blog = BlogPost.objects.get(id=self.kwargs['pk'])
        comments = BlogComment.objects.filter(blog=blog)
        likes = BlogLike.objects.filter(blog=blog)
        return render(request, self.template_name, {'post': blog, 'comments': comments,  'likes': likes})


class UserView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'posts': BlogPost.objects.filter(author=request.user)})


class UserView(ListView):
    model = BlogPost
    template_name = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'posts': BlogPost.objects.filter(author=request.user)})

class GetLikes(DetailView):
    model=BlogLike
    template_name=''
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'likes': BlogLike.objects.filter(blog__id=self.kwargs['pk'])})
class CreateLike(View, LoginRequiredMixin):
    def post(self, request, pk):
        blog = BlogPost.objects.get(pk=pk)
        BlogLike(
            blog=blog,
            like_author = request.user
        ).save()
        return JsonResponse({"status": "Success"})

class CreateComment(View, LoginRequiredMixin):
    def get(self, request, pk):
        blog = BlogPost.objects.get(pk=pk)
        return render(request, 'blog/add_comment.html', {'post': blog})
    def post(self, request, pk):
        blog = BlogPost.objects.get(pk=pk)
        comment = BlogComment(
            blog=blog,
            comment_author = request.user,
            comment_content = request.POST['content'])
        comment.save()
        return JsonResponse({"status": "Success","comment":comment})
