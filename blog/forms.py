from django import forms
from .models import Comment, Blog


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'text', 'category')
