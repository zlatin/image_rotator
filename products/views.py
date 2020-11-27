from products.serializers import ProductSerializer
from django.shortcuts import render
from rest_framework import viewsets
from products.models import Product


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
