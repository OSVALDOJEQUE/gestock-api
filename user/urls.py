from django.urls import path
from .views import UserDetails, UserView
from rest_framework.authtoken import views

urlpatterns = [
    path('',UserView.as_view(),name='url_account'),
    path('token/', views.obtain_auth_token),
    path('<int:pk>/',UserDetails.as_view(),name='userDetails'),
    path('<str:email>/', UserDetails.as_view(),name='userDetailsEmail')
]