from rest_framework.views import APIView
from .models import Sale
from rest_framework.response import Response
from .serializers import SaleSerializer
from rest_framework import  status
from django.http import Http404

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
# Create your views here.

class SaleView(APIView):
    def get(self,request,format=None):
        data = Sale.objects.all()
        serializers = SaleSerializer(data,many= True)
        return Response(serializers.data)

    def post(self, request, format=None):
        data = request.data
        serializers = SaleSerializer(data=data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class SaleDetails(APIView):

    def get_object(self,pk):
        try:
            return Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            raise Http404
    @swagger_auto_schema(responses={200: SaleSerializer(many=True)})
    def get(self,request,pk=None):
        data = self.get_object(pk)
        serializers = SaleSerializer(data)
        return Response(serializers.data)

    def put(self, request, pk=None):
        data = self.get_object(pk)
        serializers = SaleSerializer(data, data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data, status=status.HTTP_200_OK)



    
