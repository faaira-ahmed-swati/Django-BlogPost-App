from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.TextField()
    # url encoded value e.g. hello world becomes hello-world
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
