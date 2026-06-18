import os

from django.db import models
from django.urls import reverse


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
