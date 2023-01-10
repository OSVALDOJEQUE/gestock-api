from django.urls import path
from . import views



urlpatterns = [
    path('', views.StockView.as_view(),name = 'StockView'),
    path('<int:pk>/', views.StockDeatails.as_view(),name = 'StockDetails'),
    path('product/', views.StockProductView.as_view(),name = 'StockProductView'),
    path('product/<int:pk>/', views.StockProductDeatails.as_view(),name = 'StockProductDetails')
]
