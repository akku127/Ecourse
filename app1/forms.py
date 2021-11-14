from django.forms import ModelForm
from .models import Comment, video

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class AddVidForm(ModelForm):
    class Meta:
        model = video
        fields = ['title', 'videofile', 'num']