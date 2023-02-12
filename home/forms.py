from django import forms

from . models import Post

class PostUpdateForm(forms.Form):
    class Meta:
        model = Post
        fields = ('body',)