'''
@authors: Julian Nunez, Jimmy Doan
@coauth: Michael Jannain
@tester: Jose Garcia
'''
from __future__ import unicode_literals
from django.db import models
import socket
import os

DEF_IMG = 'default.png'
DEF_IMG_PATH = os.getcwd() + DEF_IMG
imgpath = os.getcwd() + 'es.jpg'

class Incident(models.Model):
    # -View Incident Record Info & Crew Info:
    #     -Record ID
    #     -Date created
    #     -Crew ID
    #     -Supervisor Name
    #     -Date on site
    #     -Scale of cleanup effort -- select from pre-defined list
    image = models.ImageField(default = DEF_IMG_PATH)
    
    record_id = models.IntegerField(default=0)
    date_created = models.DateTimeField('created date')
    crew_id = models.IntegerField(default=0)
    supervisor_name = models.CharField(max_length=100)
    date_on_site = models.DateTimeField('incident date')
    SCALE_OF_CLEANUP = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
)
    cleanup_scale = models.CharField(max_length=1, choices=SCALE_OF_CLEANUP)
    
    # -Ability to Edit Graffiti Info:
    #     -Type of building or structure
    #     -Street address of building or property
    #     -Nearest cross streets
    #     -GPS coordinates
    #     -Moniker
    #     -Number of images
    TYPE_OF_BUILDING = (
        ('I', 'Industrial'),
        ('C', 'Commercial'),
        ('R', 'Residential'),
)
    building_type = models.CharField(max_length=1, choices=TYPE_OF_BUILDING, default='I')
    property_address = models.CharField(max_length=100, default='')
    nearest_cross_street = models.CharField(max_length=100, default='')
    gps_coordinates = models.CharField(max_length=100, default='')
    moniker = models.CharField(max_length=100, default='')
    number_of_images = models.IntegerField(default=0)
    
    # Packet: x,y,z,<imgbytes,;...next packet
    def clean(self):
        print self.pk
        
        HOST = "localhost"
        PORT = 65000
        
        send_data = ''
        send_arr = []
        temp_arr = []
        count = Incident.objects.count()
        for x in range(count): # Gets the data from each instance of the incident class as string (comma sep)
            incident = Incident.objects.get(id=x+1)
            temp_arr = [str(x+1), str(incident.record_id), str(incident.date_created), 
                      str(incident.crew_id), str(incident.supervisor_name), str(incident.date_created), 
                      str(incident.cleanup_scale), str(incident.building_type), str(incident.property_address),
                      str(incident.nearest_cross_street), str(incident.gps_coordinates), str(incident.moniker),
                      str(incident.number_of_images), str(self.image)]
            send_arr.append(temp_arr)
        for x in range(len(send_arr)):
            for y in range(len(send_arr[x])):
                send_data += send_arr[x][y] + ','
            send_data += ';'
            send_data += ','
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Sends the data to the offline GUI over socket
        client.connect((HOST, PORT))
        client.sendall(send_data)
        client.shutdown(socket.SHUT_RDWR)
        client.close()
