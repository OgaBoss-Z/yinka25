from django.urls import path
from . import views
from django.urls import path
from .views import contact_view

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about-us', views.about_us, name='about-page'),
    path('services', views.services, name='service-page'),
    path('success-message', views.success_page, name='success-page'),
    path('contact-us', views.contact_view, name='contact-page'),
]