from rest_framework import serializers
from .models import StockProduct,Stock
from product.serializers import ProductSerializer
from user.serializers import UserSerializer


class StockSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Stock
        fields ='__all__'

class StockProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    stock =StockSerializer(read_only=True)
    product = ProductSerializer(read_only=True)


    class Meta:
        model = StockProduct
        fields = '__all__'
