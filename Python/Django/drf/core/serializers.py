from rest_framework import serializers
from models import User

class User(serializers.Serializer):
    user_id = serializers.IntegerField()
    firstname = serializers.CharField(max_length=200)
    middlename = serializers.CharField(max_length=200)
    lastname = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    phonenumber = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id','firstname','middlename','lastname','phonenumber']
        
