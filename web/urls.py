from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('about-us', views.about_us, name='about-page'),
    path('services', views.services, name='service-page'),
    path('projects', views.projects, name='project-page'),
    path('project-name', views.project_detail, name='project-detail-page'),
    path('contact-us', views.contact_us, name='contact-page'),
]