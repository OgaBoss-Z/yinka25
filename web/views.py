from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ContactForm
import logging 

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


def success_page(request):
    context = {'title': 'Success Page'}
    return render(request, 'web/success.html', context)


def contact_us(request):
    context = {'title': 'Contact Us'}
    return render(request, 'web/contact.html', context)


logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"From: {name} <{email}>\n\n{message}"
            try:
                send_mail(
                    subject,
                    full_message,
                    email,
                    ['yinkakayode25@gmail.com'],
                )
                return render(request, 'web/success.html')
            except Exception as e:
                print('EMAIL ERROR: ', e)
                return render(request, 'web/project.html')
        return render(request, 'web/contact.html', {'title': 'Contact Us', 'form': form})
    else:
        form = ContactForm()
        return render(request, 'web/contact.html', {'title': 'Contact Us', 'form': form})



