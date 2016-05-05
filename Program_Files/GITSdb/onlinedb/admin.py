from django.contrib import admin
from .models import Incident

class IncidentAdmin(admin.ModelAdmin):
    model = Incident

admin.site.register(Incident, IncidentAdmin)