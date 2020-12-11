import json

import pytest


@pytest.mark.django_db
def test_updated_field_changed_on_update(client, product, freezer):
    freezer.move_to("2021-03-10")
    resp = client.patch(
        f"/products/{product.uuid}/",
        {"name": "kilo goroha"},
        content_type="application/json",
    )
    got_product = json.loads(resp.content)
    assert got_product["updated"] == "2021-03-10T00:00:00Z"


@pytest.mark.django_db
def test_modified_product_CANNOT_be_modified_again(client, modified_product):
    resp = client.patch(
        f"/products/{modified_product.uuid}/",
        {"descriptoin": "stop doing it please"},
        content_type="application/json",
    )
    assert resp.status_code == 409
    details = resp.json()["details"]
    assert details == "Product editing allowed only once"
