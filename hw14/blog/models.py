import os

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category-page", args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:tag-page", args=[self.slug])


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    head_image = models.ImageField(
        upload_to="blog/images/%Y/%m/%d/",
        blank=True,
    )
    file_upload = models.FileField(
        upload_to="blog/files/%Y/%m/%d/",
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="posts",
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return f"[{self.pk}] {self.title}"

    def get_absolute_url(self):
        return reverse("blog:post-detail", args=[self.pk])

    def get_file_name(self):
        if not self.file_upload:
            return ""
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return os.path.splitext(self.get_file_name())[1].lstrip(".").lower()
