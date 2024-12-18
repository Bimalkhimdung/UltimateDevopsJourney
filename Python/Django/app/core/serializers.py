from .models import Core, Detail
from rest_framework import serializers

class UserDetail(serializers.Serializer):
    user_id = serializers.IntegerField()
    #id = serializers.IntegerField()
    lastname = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Core
        fields = ['user_id', 'firstname', 'lastname', 'email']