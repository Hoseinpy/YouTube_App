from django.forms import ValidationError


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4','.mov','.webm']
    if not ext in valid_extensions:
        message = 'please upload a valid format like .mp4, .mov, .webm'
        raise ValidationError(message)