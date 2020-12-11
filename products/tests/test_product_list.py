import json

import pytest
from mixer.backend.django import mixer
from products.models import Product


@pytest.mark.django_db
def test_products_endpoint_available(client):
    resp = client.get("/products/")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_created_product_listed(client):
    product = mixer.blend(Product)
    resp = client.get("/products/")
    results = json.loads(resp.content)["results"]
    assert len(results) == 1


@pytest.mark.django_db
def test_no_more_than_10_results_returned_per_page(client):
    products = mixer.cycle(11).blend(Product)
    resp = client.get("/products/")
    results = json.loads(resp.content)["results"]
    assert len(results) == 10


@pytest.mark.django_db
def test_modified_false_product_unmodified(client, product):
    resp = client.get("/products/?modified=false")
    results = json.loads(resp.content)["results"]
    assert len(results) == 1


@pytest.mark.django_db
def test_modified_true_product_unmodified(client, product):
    resp = client.get("/products/?modified=true")
    results = json.loads(resp.content)["results"]
    assert len(results) == 0


@pytest.mark.django_db
def test_modified_false_product_modified(client, modified_product):
    resp = client.get("/products/?modified=false")
    results = json.loads(resp.content)["results"]
    assert len(results) == 0


@pytest.mark.django_db
def test_modified_true_product_modified(client, modified_product):
    resp = client.get("/products/?modified=true")
    results = json.loads(resp.content)["results"]
    assert len(results) == 1
