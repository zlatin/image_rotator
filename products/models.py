import uuid
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File
from django.db import models
from PIL import Image
import mimetypes


class Product(models.Model):
    """
    Model for products. Logo rotated by 180 degrees on save
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    logo = models.ImageField(upload_to="logos/")
    rotate_duration = models.DurationField(blank=True, null=True)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs) -> None:
        buffer = BytesIO()
        if self.logo:
            img_file = BytesIO(self.logo.read())
            img = Image.open(img_file) 
            img = img.rotate(180)
            extension = self.logo.name.split('.')[-1]
            img.save(buffer, extension)
            buffer.seek(0)
            self.logo = File(buffer, name=self.logo.name)

        
        super(Product, self).save(*args, **kwargs)
        buffer.close()


