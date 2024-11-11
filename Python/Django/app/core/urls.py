from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.main, name='Landing page'),
    path('api/', views.api, name='api'),
    path('api/v1/', views.v1, name='v1'),
    path('users/', views.users, name='list all users'),
    path('user/', views.User_serializer, name='serilized users'),
             
    ]