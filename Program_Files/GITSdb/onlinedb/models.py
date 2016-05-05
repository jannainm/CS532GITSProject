#from django.utils.encoding import python_2_unicode_compatible
#from datetime import datetime
#import datetime
#from django.utils import timezone
from __future__ import unicode_literals
from django.db import models
#from django.core.files import File
#from cStringIO import StringIO
import socket
import os

#IMG_CODE = '1975652234'
DEF_IMG = 'default.png'
DEF_IMG_PATH = os.getcwd() + DEF_IMG
imgpath = os.getcwd() + 'es.jpg'

#@python_2_unicode_compatible
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
        print self.record_id
            
        '''
        # image bytestring for socket
        with open("es.jpg", "rb") as imageFile:
            f = imageFile.read()
            b = bytearray(f)

        print b[0]
        print b[1]
        '''
        
        #if self.image == './default.png':
        #    print "YES"
        #else:
        #    print "NO"
        
        HOST = "localhost"
        PORT = 65000
        
        send_data = ''
        send_arr = []
        temp_arr = []
        count = Incident.objects.count()
        for x in range(count):
            print x
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
            
        #print send_data
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        client.sendall(send_data)
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        
# ONLINE/OFFLINE:
# ###
# -Navigation Structure
# -User Login Management
# -Authorized Users: Information Entry/Maintenance
# -Allowable Access Areas: Subsystems
# -System Admin Menu
# -Print Authorized User Report: Whole System/Subsystem
# -System Level Authorized Users: Password Set/Initialization
# ###
# -User Name
# -User Employee Number
# -User's Job Title
# -User Password
# ###
#
# LAW ENFORCEMENT (OFFLINE):
# -View Incident Record Info & Crew Info:
#     -Record ID
#     -Date created
#     -Crew ID
#     -Supervisor Name
#     -Date on site
#     -Scale of cleanup effort--select from pre-defined list
# -Ability to Edit Graffiti Info:
#     -Type of building or structure
#     -Street address of building or property
#     -Nearest cross streets
#     -GPS coordinates
#     -Moniker
#     -Number of images
# -Ability to Update Graffiti Info:
#     -Amount of damage
#     -Status of Investigation:
#         -new, in process, in litigation, resolved
# -Ability to Update Suspect Info:
#     -Suspect name(s)
#     -Suspect info
#     -Crew or gang
#     Status: unknown, in custody, identified, released
# -Graffiti Incident Documentation (options):
#     -Submit
#     -Cancel
# -Image Upload:
#     -Browse for images
#     -Select Images for Upload
#     -Upload Button


#send_data = str(self.pk) + ',' + str(self.record_id) + ',' + str(self.date_created)
#temp = Incident.objects.all().values()
#print temp["record_id"]
#temp = Incident.objects.get(id=1)
#newtemp = getattr(temp, 'record_id')
#print newtemp
#print temp
#print Incident.objects.count()

#     
#     def loadData():
#         send_data = ''
#         send_arr = []
#         temp_arr = []
#         count = Incident.objects.count()
#         for x in range(count):
#             incident = Incident.objects.get(id=x+1)
#             temp_arr = [str(x+1), str(incident.record_id), str(incident.date_created), 
#                       str(incident.crew_id), str(incident.supervisor_name), str(incident.cleanup_scale)]
#             send_arr.append(temp_arr)
#         for x in range(len(send_arr)-1):
#             for y in range(len(send_arr[x])-1):
#                 send_data += send_arr[x][y] + ','
#             send_data += ';'