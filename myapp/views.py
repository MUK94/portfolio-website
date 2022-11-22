from django.shortcuts import render
from .models import About, Project, Skill, Learning, Service, Slider


def home(request):
    title = 'Mouctar - Portfolio'
    abouts = About.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    learnings = Learning.objects.all()
    services = Service.objects.all()
    sliders = Slider.objects.all()
    context = {
        'title' : title,
        'abouts' : abouts,
        'projects' : projects,
        'skills' : skills,
        'learnings' : learnings,
        'services' : services,
        'sliders' : sliders,
    }
    return render(request, 'base.html', context)

def detail(request, slug):
    project = Project.objects.get(slug=slug)
    title = project.title
    context = {
        'project' : project,
        'title' : title,
    }

    return render(request, 'detail.html', context)
