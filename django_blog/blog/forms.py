from django import forms
from .models import Comment
from taggit.forms import TagWidget  # Import the TagWidget for tag input
from .models import Post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include 'tags' field
        widgets = {
            'tags': TagWidget(),  # This will use the TagWidget from taggit
        }