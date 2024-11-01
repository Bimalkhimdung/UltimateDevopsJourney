from django.urls import path 
from . import views
urlpatterns = [
    path('api/', views.api, name='api'),
    path('api/v1/', views.v1, name='v1'),
    path('users/', views.users, name='list all users')
]