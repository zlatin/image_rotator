import uuid
from products.serializers import ProductSerializer
from django.shortcuts import render
from rest_framework import viewsets
from products.models import Product


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        modified = self.request.query_params.get('modified', None)
        if modified == 'true':
            products = Product.objects.filter(updated__isnull=False)
        if modified == 'false':
            products = Product.objects.filter(updated__isnull=True)
        return products
    
