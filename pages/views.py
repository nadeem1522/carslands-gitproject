from pages.models import Teams
import pages
from django.shortcuts import render
from .models import Teams

# Create your views here.
def home(request):
    Teamss = Teams.objects.all()
    data = {
        'Teamss' : Teamss,
    }
    return render(request,'pages/home.html', data)

def about(request):
    Teamss = Teams.objects.all()
    data = {
        'Teamss' : Teamss,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')    