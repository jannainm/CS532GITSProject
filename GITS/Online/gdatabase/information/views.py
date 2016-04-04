from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Information

#def index(request):
#    return HttpResponse("Hello, world. You are at the index.")

# def index(request):
#     latest_incident_list = Information.objects.order_by('-date')[:5]
#     output = ', '.join([q.incidentName for q in latest_incident_list])
#     return HttpResponse(output)

def index(request):
    latest_incident_list = Information.objects.order_by('-date')[:5]
    template = loader.get_template('information/index.html')
    context = {
        'latest_incident_list': latest_incident_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, incidentID):
    return HttpResponse("You're looking at incident %s." % incidentID)
'''
incidentID above comes from urls...where you pass in the regex and name corresponding to incidnetID
'''


# Create your views here.
