from django.shortcuts import render
from rest_framework.decorators import *
from rest_framework.response import Response
from .models import User

# Create your views here.
@api_view(['GET','POST','DELETE'])
def user(request):
        return Response({'user_id = User.objects.all(),values()'})
    
