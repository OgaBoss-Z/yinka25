from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Liat of services in the home page after the first section.
class Home_services(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='home_service_img')
    created = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Home Service Section'
        verbose_name_plural = 'Home Service Section' 
        ordering = ['name'] 

    def __str__(self):
        return self.name
    
# Home page section
class Home_what_we_do(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextUploadingField()
    real_estate = RichTextUploadingField()
    consultancy = RichTextUploadingField()
    project_mgt = RichTextUploadingField()
    property_management = RichTextField(null=True, blank=True)
    asset_valuation = RichTextUploadingField()
    project_appraisal = RichTextUploadingField()
    created = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'What We Do'
        verbose_name_plural = 'What We Do' 
        ordering = ['name']                   


    def __str__(self):
        return self.name
    
class Home_success(models.Model):
    company_name = models.CharField(max_length=100)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='home_service_img')
    created = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Home Success Section'
        verbose_name_plural = 'Home Success Section' 
        ordering = ['company_name'] 

    def __str__(self):
        return self.company_name
    

# Project page detail page
class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True, blank=True)
    pro_image = models.ImageField(upload_to='project_img')
    client = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    time_frame = models.CharField(max_length=50)
    extra_service = models.CharField(max_length=100)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project' 
        ordering = ['name'] 

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='p_img', null=True, blank=True)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)


class StaticServices(models.Model):    
    name = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='service_img')
    created = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Service Page Content'
        verbose_name_plural = 'Service Page Content' 
        ordering = ['name'] 

    def __str__(self):
        return self.name

class Services(models.Model):    
    name = models.CharField(max_length=100)
    top_description = RichTextUploadingField(null=True, blank=True)
    image = models.ImageField(upload_to='service_img')
    img_description = RichTextUploadingField(null=True, blank=True)
    created = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services' 
        ordering = ['name'] 

    def __str__(self):
        return self.name
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField()
    created = models.DateField(default=timezone.now)
    updated = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages' 
        ordering = ['name'] 

    def __str__(self):
        return self.name


