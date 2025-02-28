from django.contrib import admin
from django.urls import path,include
from . import views
from .views import MediaDirectoryView



urlpatterns = [
    path('mediaspec/', views.MediaDirectoryView.as_view(), name='media-directory'),
]