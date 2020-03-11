from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=16)
    content = HTMLField()
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_time']
