from rest_framework import serializers
import os
import shutil
from datetime import datetime
from django.urls import path


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(PROJECT_DIR, "media")
class MediaDirctorySerializer(serializers.Serializer):
    directory_path = serializers.CharField()
    total_size = serializers.CharField(required=False)
    disk_usage = serializers.DictField(required=False)
    

    def get_disk_usage(self, path):
        try:
            total, used, free = shutil.disk_usage(path)
            return {
                'total': total,
                'used': used,
                'free': free,
                'used_percent': (used / total) * 100
            }
        except Exception as e:
            return f"Error while getting disk usage, {e}"

    def get_directory_size(self, path):
        """ Calculate the total size of the media directory """
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            try:
                total_size += os.path.getsize(dirpath)
            except (OSError, FileNotFoundError):
                pass
            
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    total_size += os.path.getsize(fp)
                except (OSError, FileNotFoundError, PermissionError):
                    pass
        return total_size
    def format_size(self, size_byte):
        """Format byte size to human-readable format"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_byte < 1024.0:
                return f"{size_byte:.2f} {unit}"
            size_byte = size_byte / 1024.0
        return f"{size_byte:.2f} PB"     

    def to_representation(self, instance):
        directory_path = instance.get('directory_path', '')
        if directory_path:
            total_size = self.get_directory_size(directory_path)
            disk_usage = self.get_disk_usage(directory_path)
            representation = super().to_representation(instance)
            representation['total_size'] = self.format_size(total_size)
            representation['disk_usage'] = disk_usage
            return representation
        return {}

   