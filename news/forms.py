from attr import attrs
from .models import *
from django.forms import ModelForm
from django import forms

class AvatarForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'about_you']
        widgets = {
            'avatar': forms.URLInput(attrs={
                'class': 'my-form', 
                'id': 'avatar-id', 
                'placeholder': "Add photo"
            }),
            'about_you': forms.Textarea(attrs={
                'class': 'my-form',
                'id': 'bio-id', 
                'placeholder': "Let us know about you",
                'rows': '6'
            })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'my-form', 
                'id': 'comment-id', 
                'placeholder': "Let us know your opinion", 
                'rows': '6',
            })
        }


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['topic', 'title', 'description', 'content', 'image', 'time']
        widgets = {
            'topic': forms.Select(attrs={
                'class': 'my-form', 
            }),
            'title': forms.Textarea(attrs={
                'class': 'my-form',
                'id': 'title-area', 
                'placeholder': "Be descriptive: max 50 characters",
                'rows': '1'
            }),
            'description': forms.Textarea(attrs={
                'class': 'my-form',
                'id': 'desc-area', 
                'placeholder': "Brief explanation",
                'rows': '4'
            }),
            'content': forms.Textarea(attrs={
                'class': 'my-form',
                'id': 'content-area', 
                'placeholder': "Tell us what happened",
                'rows': '8'
            }),    
            'image': forms.URLInput(attrs={
                'class': 'my-form', 
                'id': 'news-img-area', 
                'placeholder': "Add photo"
            }),
            'time': forms.Textarea(attrs={
                'class': 'my-form',
                'id': 'time-area', 
                'placeholder': "e. g. 1900/06/02",
                'rows': '1'
            }),
        }

       