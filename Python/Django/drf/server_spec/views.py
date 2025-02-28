from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import status
import os

from .media_serializer import MediaDirctorySerializer
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(PROJECT_DIR, "media")

class MediaDirectoryView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        directory_path = request.query_params.get('directory_path', None)
        if not directory_path:
            return Response({"error": "Directory path is required"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = MediaDirctorySerializer(data={'directory_path': directory_path})
        
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)