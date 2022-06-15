from django.forms.widgets import NumberInput
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    avatar = models.URLField(max_length=180, default=None, blank=True, null=True)
    about_you = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'


class Topic(models.Model):
    topic = models.CharField(max_length=18, default=None, blank=True, null=True, unique=True)

    def __str__(self):
        return f"{self.topic}"


class Comment(models.Model):
    comment = models.CharField(max_length=500, default=None, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name="comment_profile", default=None)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_news")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False, blank=False, related_name="news_topic", default=2)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name="profile_news", default=None)
    title = models.CharField(max_length=60, default=None,blank=True, null=True)
    description = models.TextField()
    content = models.TextField(default=None,blank=True, null=True)
    image = models.URLField(max_length=180, default=None, blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True, related_name="news_comments")
    time = models.CharField(max_length=10, default=None,blank=True, null=True)
    readlist = models.ManyToManyField(User, blank=True, related_name="news_readlist")

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'topic': self.topic,
            'description': self.description,
            'content': self.content,
            'image': self.image,
            'comments': self.comments,
            'time': self.time
        }
