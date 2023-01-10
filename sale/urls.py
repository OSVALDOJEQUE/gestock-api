from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views



urlpatterns =[
    path('', views.SaleView.as_view(),name='SaleView'),
    path('<int:pk>/',views.SaleDetails.as_view(), name='SaleDetails')
]