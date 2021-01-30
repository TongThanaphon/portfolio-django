from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.utils import timezone

from .models import Profile, Project, Skill, Activity, ContactMe

def index(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    activities = Activity.objects.all()
    contacts = ContactMe.objects.order_by('-sent_date')[:3]
    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills,
        'activities': activities,
        'contacts': contacts
    }
    return render(request, 'portfolio/index.html', context)

def contact_me(request):
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    sent_date = timezone.now()

    contact_me_info = ContactMe(email = email, subject = subject, message = message, sent_date = sent_date)
    contact_me_info.save()

    return HttpResponseRedirect(reverse('portfolio:index'))
