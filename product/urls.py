import imp
from django.urls import path, include
from . import  views


urlpatterns = [
    path('',views.ProductView.as_view(), name ='url_product'),
    path('<int:pk>/',views.ProductDetails.as_view(), name = 'productDetails'),
    path('category/',views.CategoryView.as_view(),name ='categoryView'),
    path('category/<int:pk>/', views.CategoryDetails.as_view(),name = 'categoryDetails')
]