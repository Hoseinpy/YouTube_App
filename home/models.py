from django.db import models
from django.contrib.auth import get_user_model
from django.forms import ValidationError

User = get_user_model()


class VideoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return f'{self.user} -- {self.title}'
    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(VideoModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.comment


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name