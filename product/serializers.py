from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    id  = serializers.IntegerField(read_only=True)

    class Meta:
        model=Category
        fields ='__all__'

class ProductSerializer(serializers.ModelSerializer):
    id  = serializers.IntegerField(read_only=True)
    product_type = CategorySerializer(read_only=True)

    class Meta:
        model=Product
        fields = '__all__'
