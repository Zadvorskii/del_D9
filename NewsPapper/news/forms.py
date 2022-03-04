from django.forms import ModelForm
from .models import Post, Category


# Создаём модельную форму
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['heading', 'text', 'category']