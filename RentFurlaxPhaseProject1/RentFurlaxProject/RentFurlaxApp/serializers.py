from rest_framework import serializers
from .models import *

class CustomerSerialilizer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('__all__')

class CategorySerialilizer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('__all__')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model= Product
        fields=('__all__')

class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model= Invoice
        fields=('__all__')
