from django.contrib import admin
from .models import VideoModel, Comment, Category


@admin.register(VideoModel)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail', 'video', 'description')


@admin.register(Comment)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'comment')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)