'''
Created on Mar 15, 2016

@author: jannainm
'''
#
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

# View Incident Record Info & Crew Info
# Record ID
# Date created
# Crew ID
# Supervisor Name
# Date on site
# Scale of cleanup effort--select from pre-defined list

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

import Tkinter
import ttk
from PIL import ImageTk, Image
#import ctypes
import sys
import time
import socket
import threading
import multiprocessing

screenRes = [640, 480] #ctypes.windll.user32.GetSystemMetrics(0)-10, ctypes.windll.user32.GetSystemMetrics(1)-30
windowWidth = screenRes[0]
windowHeight = screenRes[1]
halfWidth = windowWidth/2; halfHeight = windowHeight/2

newGeometry = str(screenRes[0]) + "x" + str(screenRes[1])

window = Tkinter.Tk()
window.geometry(newGeometry)

##################################################################################################################################
# Notebook: sets up notebook with tabs in the middle of the main window - each tab is a frame.
##################################################################################################################################

notebook = ttk.Notebook(window)
notebook.place(relx = 0, rely = 0.5, relwidth = 1, relheight = 0.5)

tab1 = Tkinter.Frame(notebook, width=windowWidth, height=halfHeight)
tab1.place()
notebook.add(tab1, text="Output")

tab2 = Tkinter.Frame(notebook, width=windowWidth, height=halfHeight)
tab2.place()
notebook.add(tab2, text="Reporting")

tab3 = Tkinter.Frame(notebook, width=windowWidth, height=halfHeight)
tab3.place()
notebook.add(tab3, text="Law Enforcement")

# tab4 = Tkinter.Frame(notebook, width=windowWidth, height=halfHeight)
# tab4.place()
# notebook.add(tab4, text="Tab 4")
# 
# tab5 = Tkinter.Frame(notebook, width=windowWidth, height=halfHeight)
# tab5.place()
# notebook.add(tab5, text="Tab 5")
# 
# tab6 = Tkinter.Frame(notebook, width=windowWidth, height=halfHeight)
# tab6.place()
# notebook.add(tab6, text="Tab 6")

##################################################################################################################################
# Top half of main window: widget setup for the top half of the main window.
##################################################################################################################################

# Graph:
graphFrame = Tkinter.Frame(window)
graphFrame.place(relx = 0.5, rely = 0, relwidth = 0.5, relheight = 0.5)
graphCanvas = Tkinter.Canvas(graphFrame, width = halfWidth, height = halfHeight)
graphCanvas.configure(bg = 'white', relief = Tkinter.GROOVE)
graphCanvas.pack()
for x in range(halfHeight):
    graphCanvas.create_line(25 * x, 0, 25 * x, 400)
    graphCanvas.create_line(0, 25 * x, 400, 25 * x)
    
setattr(window, "graphCanvas", graphCanvas)
# End Graph

listOfIncidentsLabel = Tkinter.Label(window, text = "List of Incidents:", font = "TkDefaultFont")
listOfIncidentsLabel.grid(row = 0, column = 0, columnspan = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, sticky = "ew")

incidentsCommandListbox = Tkinter.Listbox(window, width = screenRes[0]/35, height = screenRes[0]/100)
incidentsCommandListbox.grid(row = 1, column = 0, columnspan = 2, rowspan = 3, ipadx = screenRes[1]/200, ipady = screenRes[1]/200)

saveButton = Tkinter.Button(window, text = "Save", font = ("TkDefaultFont", int(round(screenRes[0]/65))), command = lambda: saveButton(window))
saveButton.grid(row = 1, column = 2, columnspan = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, sticky = "ew")

loadButton = Tkinter.Button(window, text = "Load", font = ("TkDefaultFont", int(round(screenRes[0]/65))), command = lambda: loadButton(window))
loadButton.grid(row = 2, column = 2, columnspan = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, sticky = "ew")

clearButton = Tkinter.Button(window, text = "Clear", font = ("TkDefaultFont", int(round(screenRes[0]/65))), command = lambda: clearButton(window))
clearButton.grid(row = 3, column = 2, columnspan = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, sticky = "ew")

updateButton = Tkinter.Button(window, text = "Update", font = ("TkDefaultFont", int(round(screenRes[0]/65))), command = lambda: updateButton(window))
updateButton.grid(row = 1, column = 4, columnspan = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, sticky = "ew")

reportButton = Tkinter.Button(window, text = "Report", font = ("TkDefaultFont", int(round(screenRes[0]/65))), command = lambda: reportButton(window))
reportButton.grid(row = 2, column = 4, columnspan = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, sticky = "ew")

def reportButton(window):
    if len(window.incidentList) < 1:
        print "Please select or add a list before a report can be compiled."
        return
    x = window.incidentList["list1"]
    totalcleanups = window.incidentCount
    numpics = window.incidentCount * int(x["numberOfImagesText"])
    gang = x["monikerText"]
    
    window.outputText.insert("end", "*************************************************\n")
    window.outputText.insert("end", "Total # of cleanups: " + str(totalcleanups) + "\n")
    window.outputText.insert("end", "Total # of pictures uploaded: " + str(numpics) + "\n")
    window.outputText.insert("end", "Most popular gang: " + str(gang) + "\n")
    window.outputText.insert("end", "*************************************************\n")
            

def updateButton(window):
    window.incidentCount = 0
    #window.incidentDictionaryTab1 = {"PKID": 0, "RecordID": 0, "DateCreated": "0/0/0", "CrewID": 0, "SupervisorName": "Name", "DateOnSite": "0/0/0", "ScaleOfCleanup": "Small"}
    #window.incidentDictionaryTab1 = {"PKID": 0, "RecordID": 0, "DateCreated": "0/0/0", "CrewID": 0, "SupervisorName": "Name", 
    #                      "DateOnSite": "0/0/0", "ScaleOfCleanup": "Small", "buildingTypeText": "Industrial", "propertyAddressText": "1234 Ding St.", "nearestCrossstreetText": "1234 Dong St.", "gpsCoordinatesText": "25-56-78", 
    #                      "monikerText": "Gang", "numberOfImagesText": 0, "image": "./default.png"}
    window.incidentDictionaryTab1 = {}
    '''
    '''
    '''
    '''
    
    # Stores values in window.incidentValuesList
    indexcounter = 0
    window.incidentValuesList = []
    f = open('logging', 'r')
    buff = f.readline()
    while buff:
        print buff
        bufferChopped = buff.split(",")
        singleIncident = []
        for x in bufferChopped:
            if '.png' in x:
                window.DEFAULT_IMG = True
            if '.jpg' in x:
                window.ES_IMG = True
            if '2016' in x:
                x = x[0:4] + '/' + x[6:7] + '/' + x[9:10] # Formats and grabs the dates
                #x = x[0:10] # grabs the date only
            if x == ';':
                indexcounter += 1
                window.incidentValuesList.append(singleIncident)
                singleIncident = []
                pass
            singleIncident.append(x)
        buff = f.readline()
    f.close()
    
    print window.incidentValuesList
    
    '''
    FIX HERE....NEED TO ACCOMIDATE FOR 2 LISTS...
    '''
    tmpcount = 0
    for x in window.incidentValuesList:
        for y in x:
            window.incidentDictionaryTab1[window.parameterNameList[tmpcount]] = y
            tmpcount += 1
        window.incidentCount += 1
        #tmpcount = 0
        window.incidentList["list"+str(window.incidentCount)] = window.incidentDictionaryTab1
    window.incidentsCommandListbox.insert("end", "list"+str(window.incidentCount))
    #print window.incidentDictionaryTab1
    print window.incidentList
    '''
    window.incidentCount += 1
    window.incidentList["list"+str(window.incidentCount)] = window.incidentDictionaryTab1
    '''

def saveButton(window):
    tempList = []
    try:
        tempList.append(int(window.pkIDText.get("1.0", "end")))
        tempList.append(int(window.recordIDText.get("1.0", "end")))
        tempList.append(str(window.dateCreatedText.get("1.0", "end")))
        tempList.append(int(window.crewIDText.get("1.0", "end"))) 
        tempList.append(str(window.supervisorNameText.get("1.0", "end"))) 
        tempList.append(str(window.dateOnSiteText.get("1.0", "end")))
        tempList.append(str(window.scale_value.get()))
        tempList.append(str(window.buildingTypeText.get("1.0", "end")))
        tempList.append(str(window.propertyAddressText.get("1.0", "end")))
        tempList.append(str(window.nearestCrossstreetText.get("1.0", "end")))
        tempList.append(str(window.gpsCoordinatesText.get("1.0", "end")))
        tempList.append(str(window.monikerText.get("1.0", "end")))
        tempList.append(str(window.numberOfImagesText.get("1.0", "end")))
        print tempList
    except:
        print "Please enter proper parameters for all categories..."
        return
    window.incidentDictionaryTab1 = {} # Clear dictionary, prevents duplicate values...
    window.incidentDictionaryTab1["PKID"] = tempList.pop(0)
    window.incidentDictionaryTab1["RecordID"] = tempList.pop(0)
    window.incidentDictionaryTab1["DateCreated"] = tempList.pop(0)
    window.incidentDictionaryTab1["CrewID"] = tempList.pop(0)
    window.incidentDictionaryTab1["SupervisorName"] = tempList.pop(0)
    window.incidentDictionaryTab1["DateOnSite"] = tempList.pop(0)
    window.incidentDictionaryTab1["ScaleOfCleanup"] = tempList.pop(0)
    window.incidentDictionaryTab1["buildingTypeText"] = tempList.pop(0)
    window.incidentDictionaryTab1["propertyAddressText"] = tempList.pop(0)
    window.incidentDictionaryTab1["nearestCrossstreetText"] = tempList.pop(0)
    window.incidentDictionaryTab1["gpsCoordinatesText"] = tempList.pop(0)
    window.incidentDictionaryTab1["monikerText"] = tempList.pop(0)
    window.incidentDictionaryTab1["numberOfImagesText"] = tempList.pop(0)

    for x in window.incidentDictionaryTab1:
        if window.incidentDictionaryTab1[x] == "\n" or window.incidentDictionaryTab1[x] == 0:
            print "Please enter proper parameters for all categories..."
            return

    window.incidentCount += 1
    window.incidentList["list"+str(window.incidentCount)] = window.incidentDictionaryTab1
    window.incidentsCommandListbox.insert("end", "list"+str(window.incidentCount))
    
    # Save Law Enforcement Data
    try:
        currInc = window.incidentsCommandListbox.get(window.incidentsCommandListbox.curselection()[0])
    except:
        currInc = "list0"
    
    incidentName = str(currInc)
    arrestStatus = str(window.arrestText.get("1.0", "end"))
    aStat = arrestStatus.split('\n')[0] # Removes '\n'
    damageStatus = str(window.damageText.get("1.0", "end"))
    dStat = damageStatus.split('\n')[0]
    incidentStatus = str(window.investigationText.get("1.0", "end"))
    iStat = incidentStatus.split('\n')[0]
    suspectStatus = str(window.suspectText.get("1.0", "end"))
    sStat = suspectStatus.split('\n')[0]
    tempArrestList = [incidentName, aStat, dStat, iStat, sStat]
    window.arrestList.append(tempArrestList)
    
    print window.arrestList
    
def loadButton(window):
    if window.incidentCount == 0 or len(window.incidentList) == 0:
        print "You can not load an incident until one is created"
        return
    try:
        currInc = window.incidentsCommandListbox.get(window.incidentsCommandListbox.curselection()[0])
    except:
        print "Please select an incident first..."
        return
    
    currentIncident = window.incidentList[currInc]
    
    gps = currentIncident["gpsCoordinatesText"] # Start of section to capture graph coordinates
    gpscoords = gps.split('-')
    gps_x = gpscoords[0]
    gps_y = gpscoords[1]
    
    xcoord = 400/int(gps_x)
    ycoord = 400/int(gps_y)
    x1coord = xcoord + 10
    y1coord = ycoord + 10
    
    window.graphCanvas.create_oval(xcoord, ycoord, x1coord, y1coord, fill = 'red')
    
    if window.DEFAULT_IMG == True: # Display black image
        window.panel.config(image = window.defimg)
        window.DEFAULT_IMG = False
    elif window.ES_IMG == True: # Display supplied image
        window.panel.config(image = window.esimg)
        window.ES_IMG = False
    else:
        window.panel.config(image = '')
    
    window.pkIDText.delete("1.0", "end")
    window.recordIDText.delete("1.0", "end")
    window.dateCreatedText.delete("1.0", "end")
    window.crewIDText.delete("1.0", "end")
    window.supervisorNameText.delete("1.0", "end")
    window.dateOnSiteText.delete("1.0", "end")
    
    window.buildingTypeText.delete("1.0", "end")
    window.propertyAddressText.delete("1.0", "end")
    window.nearestCrossstreetText.delete("1.0", "end")
    window.gpsCoordinatesText.delete("1.0", "end")
    window.monikerText.delete("1.0", "end")
    window.numberOfImagesText.delete("1.0", "end")
    
    # Law Enforcement
    window.arrestText.delete("1.0", "end")
    window.damageText.delete("1.0", "end")
    window.investigationText.delete("1.0", "end")
    window.suspectText.delete("1.0", "end")
    
    # Law Enforcement - insert data if available
    if len(window.arrestList) < 5:
        for x in window.arrestList:
            if x[0] == currInc:
                window.arrestText.insert("1.0", x[1])
                window.damageText.insert("1.0", x[2])
                window.investigationText.insert("1.0", x[3])
                window.suspectText.insert("1.0", x[4])
            
    
    window.pkIDText.insert("1.0", currentIncident["PKID"])
    window.recordIDText.insert("1.0", currentIncident["RecordID"])
    window.dateCreatedText.insert("1.0", currentIncident["DateCreated"])
    window.crewIDText.insert("1.0", currentIncident["CrewID"])
    window.supervisorNameText.insert("1.0", currentIncident["SupervisorName"])
    window.dateOnSiteText.insert("1.0", currentIncident["DateOnSite"])
    window.scale_value.set(currentIncident["ScaleOfCleanup"])
    window.buildingTypeText.insert("1.0", currentIncident["buildingTypeText"])
    window.propertyAddressText.insert("1.0", currentIncident["propertyAddressText"])
    window.nearestCrossstreetText.insert("1.0", currentIncident["nearestCrossstreetText"])
    window.gpsCoordinatesText.insert("1.0", currentIncident["gpsCoordinatesText"])
    window.monikerText.insert("1.0", currentIncident["monikerText"])
    window.numberOfImagesText.insert("1.0", currentIncident["numberOfImagesText"])
    
    
def clearButton(window):
    window.incidentDictionaryTab1 = {}
    window.incidentList = {}
    window.incidentCount = 0
    window.pkIDText.delete("1.0", "end")
    window.recordIDText.delete("1.0", "end")
    window.dateCreatedText.delete("1.0", "end")
    window.crewIDText.delete("1.0", "end")
    window.supervisorNameText.delete("1.0", "end")
    window.dateOnSiteText.delete("1.0", "end")
    
    window.buildingTypeText.delete("1.0", "end")
    window.propertyAddressText.delete("1.0", "end")
    window.nearestCrossstreetText.delete("1.0", "end")
    window.gpsCoordinatesText.delete("1.0", "end")
    window.monikerText.delete("1.0", "end")
    window.numberOfImagesText.delete("1.0", "end")
    
    window.incidentsCommandListbox.delete(0, "end")
    
    window.outputText.delete("1.0", "end")
    
    # Law Enforcement Data
    window.arrestList = []
    window.arrestText.delete("1.0", "end")
    window.damageText.delete("1.0", "end")
    window.investigationText.delete("1.0", "end")
    window.suspectText.delete("1.0", "end")
    window.DEFAULT_IMAGE = False
    window.ES_IMG = False

##################################################################################################################################
# tab1: scaleOfOutputLabel: drop-down for values to select cleanup scale.
##################################################################################################################################

scaleOfOutputLabel = Tkinter.Label(tab1, text = "Cleanup Scale:", font = "TkDefaultFont")
scaleOfOutputLabel.grid(row = 7, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

def scaleUpdate(name):
    scale_value.set(name)

scales = ["Small","Medium","Large"]
scale_value = Tkinter.StringVar()
scale_value.set("")
scaleOptions = Tkinter.OptionMenu(tab1, scale_value, "")

if len(scales) > 0:
    scaleOptions["menu"].delete(0, "end")
    for scale in scales:
        scaleOptions["menu"].add_command(label=scale, command = lambda value=scale: scaleUpdate(value))
        scale_value.set(scales[0])
else:
    scaleOptions["menu"].delete(0, "end")
scaleOptions.grid(row=7,column=2, columnspan = 2, sticky = "ew")

##################################################################################################################################
# tab1: output tab
##################################################################################################################################
# -View Incident Record Info & Crew Info:
#     -Record ID
#     -Date created
#     -Crew ID
#     -Supervisor Name
#     -Date on site
#     -Scale of cleanup effort--select from pre-defined list

#dataRowOneLabel = Tkinter.Label(tab1, text = "Data Row One: ", font = "TkDefaultFont")
#dataRowOneLabel.grid(row = 0, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 4, sticky = "ew")

pkIDLabel = Tkinter.Label(tab1, text = "PK ID:", font = "TkDefaultFont")
pkIDLabel.grid(row = 1, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

# 50 instead of 200 on width
pkIDText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/50)
pkIDText.grid(row = 1, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = 'ew')

recordIDLabel = Tkinter.Label(tab1, text = "Record ID:", font = "TkDefaultFont")
recordIDLabel.grid(row = 2, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

# 50 instead of 200 on width
recordIDText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/50)
recordIDText.grid(row = 2, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = 'ew')

dateCreatedLabel = Tkinter.Label(tab1, text = "Date Created:", font = "TkDefaultFont")
dateCreatedLabel.grid(row = 3, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

dateCreatedText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/200)
dateCreatedText.grid(row = 3, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

crewIDLabel = Tkinter.Label(tab1, text = "Crew ID:", font = "TkDefaultFont")
crewIDLabel.grid(row = 4, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

crewIDText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/200)
crewIDText.grid(row = 4, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

supervisorNameLabel = Tkinter.Label(tab1, text = "Supervisor Name:", font = "TkDefaultFont")
supervisorNameLabel.grid(row = 5, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

supervisorNameText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/200)
supervisorNameText.grid(row = 5, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

dateOnSiteLabel = Tkinter.Label(tab1, text = "Date on Site:", font = "TkDefaultFont")
dateOnSiteLabel.grid(row = 6, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

dateOnSiteText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/200)
dateOnSiteText.grid(row = 6, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

buildingTypeLabel = Tkinter.Label(tab1, text = "Building Type:", font = "TkDefaultFont")
buildingTypeLabel.grid(row = 1, column = 4, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

buildingTypeText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/50)
buildingTypeText.grid(row = 1, column = 6, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

propertyAddressLabel = Tkinter.Label(tab1, text = "Property Address:", font = "TkDefaultFont")
propertyAddressLabel.grid(row = 2, column = 4, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

propertyAddressText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/50)
propertyAddressText.grid(row = 2, column = 6, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

nearestCrossstreetLabel = Tkinter.Label(tab1, text = "Cross Street:", font = "TkDefaultFont")
nearestCrossstreetLabel.grid(row = 3, column = 4, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

nearestCrossstreetText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/50)
nearestCrossstreetText.grid(row = 3, column = 6, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

gpsCoordinatesLabel = Tkinter.Label(tab1, text = "GPS:", font = "TkDefaultFont")
gpsCoordinatesLabel.grid(row = 4, column = 4, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

gpsCoordinatesText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/50)
gpsCoordinatesText.grid(row = 4, column = 6, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

monikerLabel = Tkinter.Label(tab1, text = "Moniker:", font = "TkDefaultFont")
monikerLabel.grid(row = 5, column = 4, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

monikerText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/50)
monikerText.grid(row = 5, column = 6, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

numberOfImagesLabel = Tkinter.Label(tab1, text = "Num Images:", font = "TkDefaultFont")
numberOfImagesLabel.grid(row = 5, column = 4, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

numberOfImagesText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/50)
numberOfImagesText.grid(row = 5, column = 6, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

# Image Frame on Tab1:
imgFrame = Tkinter.Frame(tab1)
imgFrame.place(relx = 0.7, rely = 0, relwidth = 0.45, relheight = 0.5)

# Image:
noimg = ''
defimg = ImageTk.PhotoImage(Image.open("default.png"))
esimg = ImageTk.PhotoImage(Image.open("es.jpg"))
panel = Tkinter.Label(imgFrame, image = noimg)
panel.pack(side = "bottom", fill = "both", expand = "yes")

##################################################################################################################################
# tab2: Reporting
##################################################################################################################################

outputText = Tkinter.Text(tab2, height = halfHeight, width = windowWidth)
outputText.grid(row = 0, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, sticky = "ew")

##################################################################################################################################
# tab3: Law Enforcement
##################################################################################################################################

arrestLabel = Tkinter.Label(tab3, text = "Arrest:", font = "TkDefaultFont")
arrestLabel.grid(row = 0, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

arrestText = Tkinter.Text(tab3, height = screenRes[0]/1000, width = screenRes[0]/50)
arrestText.grid(row = 0, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

damageLabel = Tkinter.Label(tab3, text = "Amount Damage:", font = "TkDefaultFont")
damageLabel.grid(row = 1, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

damageText = Tkinter.Text(tab3, height = screenRes[0]/1000, width = screenRes[0]/50)
damageText.grid(row = 1, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

investigationText = Tkinter.Label(tab3, text = "Investigation Status:", font = "TkDefaultFont")
investigationText.grid(row = 2, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

investigationText = Tkinter.Text(tab3, height = screenRes[0]/1000, width = screenRes[0]/50)
investigationText.grid(row = 2, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

suspectLabel = Tkinter.Label(tab3, text = "Suspect Info:", font = "TkDefaultFont")
suspectLabel.grid(row = 3, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

suspectText = Tkinter.Text(tab3, height = screenRes[0]/1000, width = screenRes[0]/50)
suspectText.grid(row = 3, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

##################################################################################################################################
# Main Variables: main variables for window and entire GUI.
##################################################################################################################################

DEBUG = False
parameterNameList = ["PKID", "RecordID", "DateCreated", "CrewID", "SupervisorName", "DateOnSite", "ScaleOfCleanup", 
                     "buildingTypeText", "propertyAddressText", "nearestCrossstreetText", "gpsCoordinatesText", 
                     "monikerText", "numberOfImagesText", "image"]

incidentDictionaryTab1 = {"PKID": 0, "RecordID": 0, "DateCreated": "0/0/0", "CrewID": 0, "SupervisorName": "Name", 
                          "DateOnSite": "0/0/0", "ScaleOfCleanup": "Small", "buildingTypeText": "Industrial", "propertyAddressText": "1234 Ding St.", "nearestCrossstreetText": "1234 Dong St.", "gpsCoordinatesText": "25-56-78", 
                          "monikerText": "Gang", "numberOfImagesText": 0, "image": "./default.png"}

incidentValuesList = [] # List of dictionaries to store incidents - e.g. just like incidentList but without param names
incidentList = {} # Main dictionary of incidents that shows in command list box
incidentCount = 0

HOST = "localhost" # Host for socket to recv from the database
PORT = 65000 # Port for socket to recv from the database
recv_data = ''
recvd_data = ''
fileArray = []
arrestList = []
lastReadTime = time.time()

FIRST_RUN = True
DEFAULT_IMG = False
ES_IMG = False

setattr(window, "DEBUG", DEBUG)
setattr(window, "incidentList", incidentList)
setattr(window, "incidentDictionaryTab1", incidentDictionaryTab1)
setattr(window, "incidentCount", incidentCount)
setattr(window, "HOST", HOST)
setattr(window, "PORT", PORT)
setattr(window, "recv_data", recv_data)
setattr(window, "recvd_data", recvd_data)
setattr(window, "FIRST_RUN", FIRST_RUN)
setattr(window, "DEFAULT_IMG", DEFAULT_IMG)
setattr(window, "ES_IMG", ES_IMG)

# Attributes from prior widgets created in sections above.
setattr(window, "incidentsCommandListbox", incidentsCommandListbox)
setattr(window, "pkIDText", pkIDText)
setattr(window, "scale_value", scale_value)
setattr(window, "dateCreatedText", dateCreatedText)
setattr(window, "dateOnSiteText", dateOnSiteText)
setattr(window, "supervisorNameText", supervisorNameText)
setattr(window, "recordIDText", recordIDText)
setattr(window, "crewIDText", crewIDText)

setattr(window, "buildingTypeText", buildingTypeText)
setattr(window, "propertyAddressText", propertyAddressText)
setattr(window, "nearestCrossstreetText", nearestCrossstreetText)
setattr(window, "gpsCoordinatesText", gpsCoordinatesText)
setattr(window, "monikerText", monikerText)
setattr(window, "numberOfImagesText", numberOfImagesText)

setattr(window, "arrestText", arrestText)
setattr(window, "damageText", damageText)
setattr(window, "investigationText", investigationText)
setattr(window, "suspectText", suspectText)
setattr(window, "arrestList", arrestList)

setattr(window, "outputText", outputText)

setattr(window, "fileArray", fileArray)
setattr(window, "lastReadTime", lastReadTime)
setattr(window, "incidentValuesList", incidentValuesList)
setattr(window, "parameterNameList", parameterNameList)

setattr(window, "noimg", noimg)
setattr(window, "defimg", defimg)
setattr(window, "esimg", esimg)
setattr(window, "panel", panel)

def onEsc(event):
    sys.exit()

def onClosing():
    window.destroy()
    
def recvSocket(): # Used by thread to run server in background
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', window.PORT))
    server.listen(5)
    while True:
        client, address = server.accept()
        print('Connection from: ', address)
        while(1):
            window.recv_data = client.recv(512)
            if not window.recv_data:
                break
            print 'RECIEVED:', window.recv_data #OR JUST ADD THESE ELEMENTS TO AN ARRY HERE EACH READ
            fd = open('logging', 'w')
            fd.write(window.recv_data)
            fd.close()
        client.shutdown(socket.SHUT_WR)
        client.close()

def readFromFile():
    f = open('logging', 'r')
    temp = f.readline()
    while temp:
        print temp
        temp = f.readline()
    f.close()

def updateGUI(window):
    # MAIN LOOP
    if window.FIRST_RUN == True:
        window.FIRST_RUN = False
        window.update()
        t = threading.Thread(target=recvSocket)
        t.start()
        #proc = multiprocessing.Process(target=recvSocket)
        #proc.start()
    window.update()
    window.after(0, func = lambda: updateGUI(window))

# binds/event handlers
window.bind("<Escape>", onEsc)
window.protocol("WM_DELETE_WINDOW", onClosing)

window.after(0, func = lambda: updateGUI(window))
window.mainloop()
