from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    #return HttpResponse("<strong>Hello World Dude<strong>")
    my_dict = {'insert': "hey I want to be inserted"}
    return render(request, 'first_app/index.html', context=my_dict)

