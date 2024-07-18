from typing import Any
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=255)
    # images = models.ImageField(upload_to='/course_images', editable=True)
    description = models.CharField(max_length=255)
    source_link = models.URLField(blank=True, null=True, max_length=200)
    
    def __str__(self):
        return str(self.name)
    
class Forum(models.Model):
    topic = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.topic)
    
class Post(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    # image = models.ImageField(upload_to='/post_images', editable=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    comment = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
