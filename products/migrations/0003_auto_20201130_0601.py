# Generated by Django 3.1.3 on 2020-11-30 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('created',)},
        ),
    ]