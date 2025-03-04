from django.urls import path 
from .views import download_video, download_progress


urlpatterns = [
    path('', download_video, name='download_video'),    
    path('download/',download_video, name='download_video'),
    path('progress/',download_video, name='download_video'),

]
