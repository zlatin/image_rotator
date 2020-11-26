from django.db import models
from django.db.models.lookups import Transform

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField
    uuid = models.UUIDField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/')
    rotate_duration = models.DurationField(blank=True, null=True)
