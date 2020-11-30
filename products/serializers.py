from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from .models import Product


class AlreadyUpdatedException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Product editing allowed only once"


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

    def update(self, instance: Product, validated_data):
        if instance.updated:
            raise AlreadyUpdatedException

        instance.updated = timezone.now()
        return super().update(instance, validated_data)
