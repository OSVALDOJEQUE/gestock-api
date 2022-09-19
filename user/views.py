from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  status
from django.http import Http404

from .serializers import UserSerializer
from .models import User

class UserView(APIView):

    def post(self,request,format=None):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def get(self,request, format=None):
        users =User.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)

class UserDetails(APIView):

    def get_object(self,pk,email):
        try:
            if email:
                return User.objects.get(email=email)
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request, pk=None, email=None, format=None):
        user=self.get_object(pk,email)
        serializer=UserSerializer(user)
        return Response(serializer.data)
    
    def put(self,request,pk, format=None):
        data=request.data
        user=self.get_object(pk)
        serializer=UserSerializer(user,data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        user =self.get_object(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
