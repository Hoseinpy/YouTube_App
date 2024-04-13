import time
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import VideoModel, Comment
from django.contrib.auth import get_user_model
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import UploadForm, CommentForm
from utils.validate_format import validate_file_extension


User = get_user_model()


def index(request):
    video = VideoModel.objects.all().order_by('-created')
    context = {'videos': video}
    return render(request, 'home/index.html', context=context)


@method_decorator([csrf_exempt], name='dispatch')
class VideoDetail(View):

    def get_video(self, video_id):
        video = get_object_or_404(VideoModel, id=video_id)
        return video

    def get(self, request, video_id):
        video = self.get_video(video_id)
        form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by('created').filter()
        
        context = {'video':video, 'form':form, 'comments':comments}
        
        return render(request, 'home/detail.html', context)

    def post(self, request, video_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                video = self.get_video(video_id)
                user_comment = form.cleaned_data.get('comment')
                c_commet = Comment.objects.create(user=request.user, video=video, comment=user_comment)

                return redirect('detail-page', video.id)
            video
            return redirect('login-page')
        
        comments = Comment.objects.filter(video=video).order_by('created').filter()
        return render(request, 'home/detail.html', {'video':video, 'form':CommentForm(), 'comments':comments})


@method_decorator([csrf_exempt, login_required()], name='dispatch')
class UploadVideo(View):
    def get(self, request):
        form = UploadForm()
        return render(request, 'home/upload_video.html', {'form':form})
    
    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():

            validate_file_extension(form.cleaned_data.get('video')) # Checks if the uploaded file is a video or not

            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            thumbnail = form.cleaned_data.get('thumbnail')
            print(f'file name {thumbnail}')
            video = form.cleaned_data.get('video')
            
            c_video = VideoModel.objects.create(user=request.user, title=title, description=description,
                                                thumbnail=thumbnail, video=video)
            time.sleep(1.5)
            return redirect('index-page')
        
        return HttpResponse(form.errors)