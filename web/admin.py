from django.contrib import admin
from .models import *

# Register your models here.
class Home_servicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
admin.site.register(Home_services, Home_servicesAdmin)


class Home_what_we_doAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
admin.site.register(Home_what_we_do, Home_what_we_doAdmin)


class Home_successAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'created', 'updated']
admin.site.register(Home_success, Home_successAdmin)


class ImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'client', 'year', 'created', 'updated']
    inlines = [ImageInline]
admin.site.register(Projects, ProjectsAdmin)


class StaticServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
admin.site.register(StaticServices, StaticServicesAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']
admin.site.register(Services, ServicesAdmin)




