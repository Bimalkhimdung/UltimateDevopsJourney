from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Core
from .serializers import * 
from django.http import JsonResponse



#after making this view change it to urlaptterns of urls.py of same app
# path = your api path in browser
# view.name_of_function {api} 
def api(request):
    return HttpResponse("This api from django api call ")

def v1(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def users(request):
    user = Core.objects.all().values()   
    template = loader.get_template('user.html')
    context = {
        'users': user,
    }
    # here is context is important for saving and sending data to template
    # users holds the data of user and send to template for loop here.
    return HttpResponse(template.render(context, request))
# route to main page

def main(request):
    
    template = loader.get_template('main.html')
    return HttpResponse(template.render)
def User_serializer(request):
    try:
        user_data = Core.objects.all()
        serializer = UserDetail(user_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    except Exception as e:
        print(f"error: {e}" )
        return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


