from django.contrib import admin
from django.contrib import admin
from .models import About, Project, Skill, Learning, Service, Slider

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'photo', 'description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'stack', 
        'publish', 'created', 'updated', 'status')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Skill)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('description', 'logo')

@admin.register(Learning)
class LearningAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_logo')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('heading', 'body', 'fullName', 'address')