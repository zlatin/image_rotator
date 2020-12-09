import json
from io import BytesIO

import pytest
from PIL import Image, ImageChops
from rest_framework.status import HTTP_201_CREATED


@pytest.fixture
def image():
    with open("./products/tests/test_data/test_image.jpg") as img_data:
        return img_data


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
