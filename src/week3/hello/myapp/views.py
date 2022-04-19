from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')
    
def greet(request, name: str):
    return render(request, 'myapp/greet.html', {
        'name': name.capitalize()
    })