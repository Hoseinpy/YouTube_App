import time
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import VideoModel, Comment, Category
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
    def get(self, request, video_id):
        video = get_object_or_404(VideoModel, id=video_id)
        form = CommentForm()
        comments = Comment.objects.filter(video=video).order_by('-created').filter()
        context = {'video':video, 'form':form, 'comments':comments}

        return render(request, 'home/detail.html', context)

    def post(self, request, video_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                video = get_object_or_404(VideoModel, id=video_id)
                comment = form.cleaned_data.get('comment')

                c_comment = Comment.objects.create(user=request.user, video=video, comment=comment)
                return redirect('detail-page', video_id)

            return redirect('login-page')

        return redirect('detail-page', video_id)


@method_decorator([csrf_exempt, login_required()], name='dispatch')
class UploadVideo(View):
    def get(self, request):
        form = UploadForm()
        categories = Category.objects.all()
        return render(request, 'home/upload_video.html', {'form':form, 'categories':categories})
    
    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():

            validate_file_extension(form.cleaned_data.get('video')) # Checks if the uploaded file is a video or not

            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            thumbnail = form.cleaned_data.get('thumbnail')
            video = form.cleaned_data.get('video')
            cat = request.POST.get('category')
            category = Category.objects.filter(name=cat).first()

            video = VideoModel.objects.create(user=request.user, title=title, description=description,
                                                thumbnail=thumbnail, video=video, category=category)

            time.sleep(1.5)
            return redirect('index-page')
        
        return HttpResponse(form.errors)

