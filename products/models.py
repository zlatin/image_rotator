import math
import uuid
from io import BytesIO
from timeit import default_timer as timer

from django.core.files import File
from django.db import models
from PIL import Image


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
        buffer = BytesIO()
        if self.logo:
            img_file = BytesIO(self.logo.read())
            img = Image.open(img_file)

            start_time = timer()

            img = img.rotate(180)

            finish_time = timer()
            rotation_duration = finish_time - start_time
            rotation_duration_seconds = math.ceil(rotation_duration)
            self.rotate_duration = rotation_duration_seconds

            extension = self.logo.name.split(".")[-1]
            img.save(buffer, extension)
            buffer.seek(0)
            self.logo = File(buffer, name=self.logo.name)

        super(Product, self).save(*args, **kwargs)
        buffer.close()
