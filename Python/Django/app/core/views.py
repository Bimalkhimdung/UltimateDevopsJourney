from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Core



#after making this view change it to urlaptterns of urls.py of same app
# path = your api path in browser
# view.name_of_function {api} 
def api(request):
    return HttpResponse("This api from dango api call ")

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


