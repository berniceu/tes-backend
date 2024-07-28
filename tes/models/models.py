from django.utils import timezone
from typing import Any
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.first_name)
    

class AccountEmail(models.Model):
    email = models.EmailField(max_length=255)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.email)


class ResetPassword(models.Model):
    email = models.EmailField(max_length=255)
    code = models.CharField(max_length=6)
    expires = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.email)
    
class ResetPasswordConfirmation(models.Model):
    email = models.EmailField(max_length=255)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.email)


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
