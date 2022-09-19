from django.urls import path
from .views import UserDetails, UserView

urlpatterns = [
    path('',UserView.as_view(),name='url_account'),
    path('<int:pk>/',UserDetails.as_view(),name='userDetails'),
    path('<str:email>/', UserDetails.as_view(),name='userDetailsEmail')
]