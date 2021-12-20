from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .models import BlogPost

from .forms import BlogForm

class CreateBlog(LoginRequiredMixin, CreateView):
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('')  # Change to get_success_url and redirect to blog detail view

    def form_valid(self, form):
        form.instance.user = self.request.user  #Make owner as logged in user
        return super().form_valid(form)

class UpdateBlog(LoginRequiredMixin, UpdateView):
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('')  # Change to get_success_url and redirect to blog detail view
    
    def get_queryset(self, **kwargs):
        qs = BlogPost.objects.filter(id=self.kwargs['pk'])
        if self.request.user == qs[0].user: #if blog is owned by user
            return qs
        return qs.none()

class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('home')  # Change to whatever is home