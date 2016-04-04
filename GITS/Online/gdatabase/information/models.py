from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Information(models.Model):
    incidentName = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    recordID = models.IntegerField()
    crewID = models.IntegerField()
    supervisorName = models.CharField(max_length=200)
    dateOnSite = models.CharField(max_length=200)
    
    def __str__(self):
        return self.incidentName
    