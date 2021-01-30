from django.contrib import admin

from .models import Profile, Skill, Project, Activity, ContactMe

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Activity)
admin.site.register(ContactMe)