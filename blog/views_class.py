import re
from django.http.response import Http404
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import BlogPost
from django.views import View
from django.shortcuts import redirect
from .forms import BlogForm


class CreateBlog(LoginRequiredMixin, View):
    form_class = BlogForm
    template_name = 'blog/crud_post.html'
    # reverse_lazy('')  # Change to get_success_url and redirect to blog detail view
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return render(request, 'blog/crud_post.html', {'mode':"Create"})
        
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        image = request.FILES.get('image', None)
        blog = BlogPost.objects.create(author=request.user, title=title, content=content, image=image)
        blog.save()
        return redirect('blog_detail', pk=blog.id)


class UpdateBlog(LoginRequiredMixin, UpdateView):
    template_name = 'blog/crud_post.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        qs = BlogPost.objects.get(id=self.kwargs['pk'])
        title = qs.title
        content = qs.content
        image = qs.image
        if request.user == qs.author:
            return render(request, 'blog/crud_post.html', {'mode':"Edit", "title": title, "content":content, "image":image})
        raise Http404
    def post(self, request, *args, **kwargs):
        blog = BlogPost.objects.get(id=self.kwargs['pk'])
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        image = request.FILES.get('image', None)
        if title == None:
            title = blog.title
        if content == None:
            content = blog.content
        if image == None:
            image = blog.image
        blog.title = title
        blog.content = content
        blog.image = image
        blog.save()
        return redirect('blog_detail', pk=blog.id)


class DeleteBlog(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        b = BlogPost.objects.filter(author=request.user, id=self.kwargs['pk'])
        if not b.exists():
            return redirect('home')
        b.delete()
        return redirect('my_blogs')
