import datetime
import json
from datetime import datetime

from django.urls import reverse
from freezegun import freeze_time
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APITestCase

from products.models import Product


@freeze_time("2020-11-13")
class ProductsCRUDTestCase(APITestCase):
    def test_products_endpoint_returns_200(self):
        response = self.client.get(reverse("product-list"))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_product_detail_returns_all_fields(self):
        product = Product.objects.create(name="test1", description="fat")
        r = self.client.get(reverse("product-list"))
        product_received = json.loads(r.content)['results'][0]
        self.assertEqual(
            product_received,
            {
                "uuid": str(product.uuid),
                "name": "test1",
                "description": "fat",
                "created": '2020-11-13T00:00:00Z',
                "updated": None,
                "logo": None,
                "rotate_duration": None,
            },
        )
