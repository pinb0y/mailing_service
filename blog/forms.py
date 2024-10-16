from django.forms import ModelForm

from blog.models import Blog
from mail_sender.forms import StyleFormMixin


class BlogForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
