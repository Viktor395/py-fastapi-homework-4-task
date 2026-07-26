import re
from datetime import date


from fastapi import UploadFile

from database.models.accounts import GenderEnum


def validate_gender(gender: str):
    
    pass


from datetime import date

def validate_birth_date(birth_date: date):
    
    return birth_date


def validate_name(name: str):
    if re.search(r'^[A-Za-z]*$', name) is None:
        raise ValueError(f'{name} contains non-english letters')


def validate_image(avatar: UploadFile) -> None:
    allowed_types = {
        "image/jpeg",
        "image/jpg",
        "image/png",
    }

    max_file_size = 1 * 1024 * 1024

    contents = avatar.file.read()

    if len(contents) > max_file_size:
        avatar.file.seek(0)
        raise ValueError("Image size exceeds 1 MB")

    avatar.file.seek(0)

    if avatar.content_type not in allowed_types:
        raise ValueError("Invalid image format")
