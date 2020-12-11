from PIL import Image, ImageChops


def images_eqal(img_got: Image, img_expected: Image):
    diff = ImageChops.difference(img_got, img_expected)
    difference_box = diff.getbbox()
    return difference_box is None