from django.urls import path
from .views import index, VideoDetail, UploadVideo

urlpatterns = [
    path('', index, name='index-page'),
    path('video/<int:video_id>', VideoDetail.as_view(), name='detail-page'),
    path('video/upload', UploadVideo.as_view(), name='upload-video-page')
]