from django.shortcuts import render
from django.http import HttpResponse

from .models import Profile, Project, Skill, Activity

def index(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    activities = Activity.objects.all()
    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills,
        'activities': activities
    }
    return render(request, 'portfolio/index.html', context)

def contact_me(request):
    response = "Contact me"
    return HttpResponse(response)
