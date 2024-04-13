from django.contrib import admin
from .models import VideoModel, Comment


@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail', 'video', 'description')


@admin.register(Comment)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'comment')