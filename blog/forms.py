from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ("title", "content", "image")
        widgets = {
            'title': forms.Textarea(attrs={'cols': 50, 'rows': 1, 'class':'form-control', 'placeholder':"Enter Title"}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 3, 'class':'form-control', 'placeholder':"Enter contents of blog"}),
        }
        