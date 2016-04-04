'''from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    # The username for the user, checks authentication, etc.
    username = models.CharField(max_length=60)

    def __unicode__(self):
        return self.username

class UserAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access = models.BooleanField()'''

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class HostGroup(models.Model):
    name = models.CharField(max_length=60, unique=True)
    active = models.BooleanField()
    date_created = models.DateTimeField('date created')

    def __unicode__(self):
        return self.name

class Computer(models.Model):
    name = models.CharField(max_length=60)
    host_group = models.ForeignKey(HostGroup)
    active = models.BooleanField()
    date_created = models.DateTimeField('date created')

    def __unicode__(self):
        return self.name
