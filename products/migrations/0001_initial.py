# Generated by Django 3.1.3 on 2020-11-26 19:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("logo", models.ImageField(upload_to="logos/")),
                ("rotate_duration", models.DurationField(blank=True, null=True)),
            ],
        ),
    ]
