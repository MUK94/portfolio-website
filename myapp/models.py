from django.db import models
from django.urls import reverse
from django.utils import timezone

class About(models.Model):
    heading = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='about/img')
    description = models.CharField(max_length=150)

class Project(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'), ('published', 'Published')
        )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    image = models.ImageField(upload_to='projects/img')
    body = models.TextField()
    github = models.URLField(blank=True)
    demo = models.URLField(blank=True)
    stack = models.CharField(max_length=100, blank=False)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    
    class Meta:
        ordering = ('-publish', )

    def __str___(self):
        return self.title
    
    # Absolute URL
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])

class Skill(models.Model):
    description = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='skill/img')


class Learning(models.Model):
    skill_name = models.CharField(max_length=70)
    skill_logo = models.ImageField(upload_to='skill/img')

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='service/img')

class Slider(models.Model):
    heading = models.CharField(max_length=70)
    body = models.TextField()
    fullName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    profile = models.ImageField(upload_to='slider/img')



