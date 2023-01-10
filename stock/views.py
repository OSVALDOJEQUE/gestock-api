from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from .models import StockProduct,Stock
from .serializers import StockSerializer,StockProductSerializer


class StockView(APIView):

    def get(self, request,format=None):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data =request.data
        serializer = StockSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class StockDeatails(APIView):

    def get_object(self,pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request,pk=None):
        stock = self.get_object(pk=pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

class StockProductView(APIView):

    def get(self, request,format=None):
        stock = StockProduct.objects.all()
        serializer = StockProductSerializer(stock,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        data =request.data
        serializer = StockProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class StockProductDeatails(APIView):

    def get_object(self,pk):
        try:
            return StockProduct.objects.get(pk=pk)
        except StockProduct.DoesNotExist:
            raise Http404

    def get_object_stock(self,pk):
        try:
            return StockProduct.objects.get(pk=pk)
        except StockProduct.DoesNotExist:
            raise Http404


    def get(self, request,pk=None):
        stock = self.get_object(pk=pk)
        serializer = StockProductSerializer(stock)
        return Response(serializer.data)




