from django.db import models
from django.utils import timezone

class Profile(models.Model):
    first_name = models.CharField('first name', max_length=200)
    last_name = models.CharField('last name', max_length=200)
    nickname = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    image = models.ImageField(blank=True, null=True)
    birth_date = models.DateField('birth date')

    def __str__(self):
        return '%s %s (%s)' % (self.first_name, self.last_name, self.nickname)

class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s - %s %s' % (self.name, self.owner.first_name, self.owner.last_name)

class Project(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return '%s - %s %s' % (self.name, self.owner.first_name, self.owner.last_name)


class Activity(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return '%s - %s %s' % (self.name, self.owner.first_name, self.owner.last_name)

class ContactMe(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    sent_date = models.DateTimeField('sent date')

    def __str__(self):
        return self.subject