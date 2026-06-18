from django.views.generic import DetailView, ListView

from .models import Post


class PostList(ListView):
    model = Post
    ordering = "-pk"


class PostDetail(DetailView):
    model = Post
