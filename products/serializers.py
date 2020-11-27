from django.db.models import fields
from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "uuid",
            "name",
            "description",
            "created",
            "updated",
            "logo",
            "rotate_duration",
        )
        read_only_fields = ("uuid", "created", "updated", "rotate_duration")
