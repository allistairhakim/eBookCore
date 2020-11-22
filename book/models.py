from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    cover = models.CharField(max_length=2000, default="")
    title = models.CharField(max_length=200, default="")
    content = models.CharField(max_length=2000, default="")
    categories = models.CharField(max_length=300, default="")
    likes = models.ManyToManyField(User, related_name="book_posts")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
