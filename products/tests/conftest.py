import pytest
from django.utils import timezone
from mixer.backend.django import mixer
from products.models import Product


@pytest.fixture
def product():
    return mixer.blend(Product)


@pytest.fixture
def modified_product(product):
    product.updated = timezone.now()
    product.save()
    return product
