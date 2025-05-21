from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    services = Home_services.objects.order_by('?')[:3]
    success_story = Home_success.objects.order_by('?')[:1]
    what_we_do = Home_what_we_do.objects.all()[:1]
    context = {
        'title': 'Home',
        'services' : services,
        'success_story': success_story,
        'what_we_do' : what_we_do,
        }
    return render(request, 'web/home.html', context)


def about_us(request):
    context = {'title': 'About Us'}
    return render(request, 'web/about.html', context)


def services(request):
    services = Services.objects.all()
    service_top = StaticServices.objects.all()
    context = {
        'title': 'Services',
        'services': services,
        'service_top': service_top,
        }
    return render(request, 'web/services.html', context)


def projects(request):
    context = {'title': 'Project'}
    return render(request, 'web/project.html', context)


def contact_us(request):
    context = {'title': 'Contact Us'}
    return render(request, 'web/contact.html', context)



def project_detail(request):
    return render(request, 'web/project-detail.html')

