import math
from io import BytesIO
from timeit import default_timer as timer

from django.core.files import File
from PIL import Image


def get_duration(f):
    """
    Measures function execution time.
    Returns tuple:
    first item is function execution duration (in seconds, ceiled),
    second item is measured function return value
    """

    def wrap(*args, **kwargs):
        start_time = timer()
        ret = f(*args, **kwargs)
        finish_time = timer()
        rotation_duration = finish_time - start_time
        rotation_duration_seconds = math.ceil(rotation_duration)
        return rotation_duration_seconds, ret

    return wrap


def rotate_image(image_to_rotate, angle):
    img = Image.open(image_to_rotate)
    img_name = image_to_rotate.name
    img = img.rotate(angle)
    extension = img_name.split(".")[-1]
    image_format = 'JPEG' if extension.lower() == 'jpg' else extension.upper()
    buffer = BytesIO()
    img.save(buffer, image_format)
    buffer.seek(0)
    rotated = File(buffer, img_name)
    img.close()
    return rotated
