from asyncore import read
from rest_framework import serializers
from .models import Sale
from product.serializers import ProductSerializer


class SaleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product = ProductSerializer(read_only=True)



    class Meta:
        model = Sale
        fields = '__all__'