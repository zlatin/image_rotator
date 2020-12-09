import pytest
from products.utils import rotate_image, get_duration
from PIL import Image, ImageChops
import shutil


def test_image_rotation_by_180():
    test_file = open("./products/tests/test_data/test_image.jpg", "rb")
    expected_image = Image.open("./products/tests/test_data/expected.jpg")
    rotated_image_file = rotate_image(test_file, 180)
    rotated_image = Image.open(rotated_image_file.file)
    diff = ImageChops.difference(expected_image, rotated_image)
    test_file.close()
    assert diff.getbbox() is None


def test_get_duration_returns_tuple_of_int_and_result():
    testfunc = lambda x: x + x
    duration, result = get_duration(testfunc)(2)
    assert isinstance(duration, int)
    assert duration >= 0
    assert result == 4
