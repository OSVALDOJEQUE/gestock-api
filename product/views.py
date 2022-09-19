from ast import Delete
from itertools import product
from unicodedata import category
from .models import Category, Product
from .serializers import CategorySerializer,ProductSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import  status
from django.http import Http404
from rest_framework.response import Response

from pprint import pprint

from product import serializers


class CategoryView(APIView):
    def get(self,request,format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
class CategoryDetails(APIView):
    def get_object(self,pk):
        try:
            return  Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self,request, pk=None):
        category =self.get_object(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request,pk,format=None):
        data =request.data
        category = self.get_object(pk=pk)
        serializer = CategorySerializer(category, data =data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk, format=None):
        category = self.get_object(pk=pk)
        category.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class  ProductView(APIView):
    def get (self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = ProductSerializer(data=data)
        pprint(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class  ProductDetails(APIView):

    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    def get(self, request,pk=None):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self,request,pk,format=None,):
        data = request.data
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status =status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None, format=None):
        category = self.get_object(pk=pk)
        category.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



        
        


