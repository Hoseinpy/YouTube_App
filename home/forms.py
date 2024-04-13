from django import forms


class UploadForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, max_length=400)
    thumbnail = forms.ImageField()
    video = forms.FileField()


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=200, required=True, label='')