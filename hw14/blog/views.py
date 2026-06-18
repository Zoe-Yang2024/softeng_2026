from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Category, Post, Tag


def taxonomy_context():
    return {
        "categories": Category.objects.all(),
        "all_post_count": Post.objects.count(),
        "no_category_post_count": Post.objects.filter(category=None).count(),
    }


class PostList(ListView):
    model = Post
    ordering = "-pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(taxonomy_context())
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(taxonomy_context())
        return context


def category_page(request, slug):
    context = taxonomy_context()
    if slug == "no-category":
        context.update(
            {
                "category_name": "미분류",
                "post_list": Post.objects.filter(category=None),
            }
        )
    else:
        category = get_object_or_404(Category, slug=slug)
        context.update(
            {
                "category": category,
                "category_name": category.name,
                "post_list": Post.objects.filter(category=category),
            }
        )
    return render(request, "blog/post_list.html", context)


def tag_page(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    context = taxonomy_context()
    context.update(
        {
            "tag": tag,
            "post_list": Post.objects.filter(tags=tag),
        }
    )
    return render(request, "blog/post_list.html", context)
