from datetime import datetime
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
import json
from rest_framework.test import APITestCase

from products.models import Product

import datetime
import json

class ProductsCRUDTestCase(APITestCase):
    def test_products_endpoint_returns_200(self):
        response = self.client.get(reverse("product-list"))
        self.assertEqual(response.status_code, HTTP_200_OK)

    # def test_product_detail_returns_all_fields(self):
    #     creation_time = datetime.datetime.now()
    #     product = Product.objects.create(
    #         name="test1", description="fat", logo="/logo/img.jpg", created=creation_time
    #     )
    #     r = self.client.get(reverse("product-list"))
    #     product_received = json.loads(r.content, object_hook=date_hook)[0]
    #     product_received.created = 
    #     self.assertEqual(
    #         product_received.uu,
    #         {
    #             "uuid": str(product.uuid),
    #             "name": "test1",
    #             "description": "fat",
    #             "created": creation_time,
    #             "updated": None,
    #             "logo": "http://testserver/media/logo/img.jpg",
    #             "rotate_duration": None,
    #         },
    #     )
