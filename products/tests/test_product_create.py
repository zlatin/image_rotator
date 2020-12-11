import json
import os
from products.tests.utils import images_eqal


import pytest
from PIL import Image
from rest_framework.status import HTTP_201_CREATED


@pytest.mark.django_db
def test_product_created_has_all_fields(client):
    with open("./products/tests/test_data/test_image.jpg", "rb") as img_data:
        resp = client.post(
            "/products/",
            {"name": "korobka vanili", "description": "squared", "logo": img_data},
            format="multipart",
        )

    assert resp.status_code == HTTP_201_CREATED

    returned_product = json.loads(resp.content)

    assert "uuid" in returned_product
    assert "name" in returned_product
    assert "description" in returned_product
    assert "created" in returned_product
    assert "updated" in returned_product
    assert "logo" in returned_product
    assert "rotate_duration" in returned_product


@pytest.mark.django_db
def test_image_rotated_on_create(client, settings):
    with open("./products/tests/test_data/test_image.jpg", "rb") as img_data:
        resp = client.post(
            "/products/",
            {"name": "korobka vanili", "description": "squared", "logo": img_data},
            format="multipart",
        )

        returned_product = json.loads(resp.content)
        logo_path = returned_product["logo"]
        logo_img_name = logo_path.split("/")[-1]
        saved_image_path = os.path.join(settings.MEDIA_ROOT, "logos", logo_img_name)
        saved_image = Image.open(saved_image_path)
        expected_image = Image.open("./products/tests/test_data/expected.jpg")
        assert images_eqal(saved_image, expected_image)
