from django.contrib import admin
from .models import Incident

admin.site.site_title = 'Crew Input Database'

class IncidentAdmin(admin.ModelAdmin):
    model = Incident

admin.site.register(Incident, IncidentAdmin)