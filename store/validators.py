from django.core.validators import ValidationError


def validate_file_size(file):
    max_file_size = 1024

    if file.size > max_file_size * 1024:
        raise ValidationError(f'Image size should be less than {max_file_size}KB')
