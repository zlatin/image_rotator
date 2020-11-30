import uuid

from django.db import models

from .utils import get_duration, rotate_image


class Product(models.Model):
    """
    Model for products. Logo rotated by 180 degrees on save
    """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, help_text="Name of the product")
    description = models.TextField(default="", help_text="Product description")
    created = models.DateTimeField(auto_now_add=True, help_text="Product creation time")
    updated = models.DateTimeField(
        blank=True, null=True, help_text="Time of product update"
    )
    logo = models.ImageField(
        blank=True,
        upload_to="logos/",
        help_text="Product logo, rotated by 180 degrees on upload",
    )
    rotate_duration = models.PositiveIntegerField(
        blank=True, null=True, help_text="Duration of image rotation in seconds, ceiled"
    )

    class Meta:
        ordering = ("created",)

    def save(self, *args, **kwargs) -> None:
        if self.logo:
            rotation_duration_seconds, rotated_image = get_duration(rotate_image)(
                self.logo, 180
            )

            self.rotate_duration = rotation_duration_seconds
            self.logo = rotated_image

        super(Product, self).save(*args, **kwargs)
