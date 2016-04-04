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
import ctypes
import sys
import time

screenRes = [640, 480]#ctypes.windll.user32.GetSystemMetrics(0)-10, ctypes.windll.user32.GetSystemMetrics(1)-30
windowWidth = screenRes[0]
windowHeight = screenRes[1]
halfWidth = windowWidth/2; halfHeight = windowHeight/2

newGeometry = str(screenRes[0]) + "x" + str(screenRes[1])
#print newGeometry

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
notebook.add(tab3, text="Tab 3")

tab4 = Tkinter.Frame(notebook, width=windowWidth, height=halfHeight)
tab4.place()
notebook.add(tab4, text="Tab 4")

tab5 = Tkinter.Frame(notebook, width=windowWidth, height=halfHeight)
tab5.place()
notebook.add(tab5, text="Tab 5")

tab6 = Tkinter.Frame(notebook, width=windowWidth, height=halfHeight)
tab6.place()
notebook.add(tab6, text="Tab 6")

##################################################################################################################################
# top half of main window: widget setup for the top half of the main window.
##################################################################################################################################

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

def saveButton(window):
    tempList = []
    try:
        tempList.append(int(window.recordIDText.get("1.0", "end")))
        tempList.append(str(window.dateCreatedText.get("1.0", "end")))
        tempList.append(int(window.crewIDText.get("1.0", "end"))) 
        tempList.append(str(window.supervisorNameText.get("1.0", "end"))) 
        tempList.append(str(window.dateOnSiteText.get("1.0", "end")))
        tempList.append(str(window.scale_value.get()))
        print tempList
    except:
        print "Please enter proper parameters for all categories..."
        return
    window.incidentDictionaryTab1 = {} # clear dictionary, prevents duplicate values...
    window.incidentDictionaryTab1["RecordID"] = tempList.pop(0)
    window.incidentDictionaryTab1["DateCreated"] = tempList.pop(0)
    window.incidentDictionaryTab1["CrewID"] = tempList.pop(0)
    window.incidentDictionaryTab1["SupervisorName"] = tempList.pop(0)
    window.incidentDictionaryTab1["DateOnSite"] = tempList.pop(0)
    window.incidentDictionaryTab1["ScaleOfCleanup"] = tempList.pop(0)
    for x in window.incidentDictionaryTab1:
        if window.incidentDictionaryTab1[x] == "\n" or window.incidentDictionaryTab1[x] == 0:
            print "Please enter proper parameters for all categories..."
            return

    window.incidentCount += 1
    window.incidentList["list"+str(window.incidentCount)] = window.incidentDictionaryTab1
    window.incidentsCommandListbox.insert("end", "list"+str(window.incidentCount))
    
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
    
    window.recordIDText.delete("1.0", "end")
    window.dateCreatedText.delete("1.0", "end")
    window.crewIDText.delete("1.0", "end")
    window.supervisorNameText.delete("1.0", "end")
    window.dateOnSiteText.delete("1.0", "end")
    
    window.recordIDText.insert("1.0", currentIncident["RecordID"])
    window.dateCreatedText.insert("1.0", currentIncident["DateCreated"])
    window.crewIDText.insert("1.0", currentIncident["CrewID"])
    window.supervisorNameText.insert("1.0", currentIncident["SupervisorName"])
    window.dateOnSiteText.insert("1.0", currentIncident["DateOnSite"])
    window.scale_value.set(currentIncident["ScaleOfCleanup"])
    
def clearButton(window):
    window.incidentDictionaryTab1 = {}
    window.incidentList = {}
    window.recordIDText.delete("1.0", "end")
    window.dateCreatedText.delete("1.0", "end")
    window.crewIDText.delete("1.0", "end")
    window.supervisorNameText.delete("1.0", "end")
    window.dateOnSiteText.delete("1.0", "end")
    window.incidentsCommandListbox.delete(0, "end")
    

##################################################################################################################################
# tab1: scaleOfOutputLabel: drop-down for values to select cleanup scale.
##################################################################################################################################

scaleOfOutputLabel = Tkinter.Label(tab1, text = "Cleanup Scale:", font = "TkDefaultFont")
scaleOfOutputLabel.grid(row = 5, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

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
scaleOptions.grid(row=5,column=2, columnspan = 2, sticky = "ew")

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

recordIDLabel = Tkinter.Label(tab1, text = "Record ID:", font = "TkDefaultFont")
recordIDLabel.grid(row = 0, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

recordIDText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/200)
recordIDText.grid(row = 0, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = 'ew')

dateCreatedLabel = Tkinter.Label(tab1, text = "Date Created:", font = "TkDefaultFont")
dateCreatedLabel.grid(row = 1, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

dateCreatedText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/200)
dateCreatedText.grid(row = 1, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

crewIDLabel = Tkinter.Label(tab1, text = "Crew ID:", font = "TkDefaultFont")
crewIDLabel.grid(row = 2, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

crewIDText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/200)
crewIDText.grid(row = 2, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

supervisorNameLabel = Tkinter.Label(tab1, text = "Supervisor Name:", font = "TkDefaultFont")
supervisorNameLabel.grid(row = 3, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

supervisorNameText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/200)
supervisorNameText.grid(row = 3, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

dateOnSiteLabel = Tkinter.Label(tab1, text = "Date on Site:", font = "TkDefaultFont")
dateOnSiteLabel.grid(row = 4, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "e")

dateOnSiteText = Tkinter.Text(tab1, height = screenRes[0]/1000, width = screenRes[0]/200)
dateOnSiteText.grid(row = 4, column = 2, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, columnspan = 2, sticky = "ew")

#outputText = Tkinter.Text(tab1, height = halfHeight, width = windowWidth)
#outputText.grid(row = 0, column = 0, ipadx = screenRes[1]/200, ipady = screenRes[1]/200, sticky = "ew")

##################################################################################################################################
# main variables: main variables for window and entire GUI.
##################################################################################################################################

DEBUG = False
incidentDictionaryTab1 = {"RecordID": 0, "DateCreated": "0/0/0", "CrewID": 0, "SupervisorName": "Name", "DateOnSite": "0/0/0", "ScaleOfCleanup": "Small"}
incidentList = {} # main sictionary of incidents that shows in command list box
incidentCount = 0

setattr(window, "DEBUG", DEBUG)
setattr(window, "incidentList", incidentList)
setattr(window, "incidentDictionaryTab1", incidentDictionaryTab1)
setattr(window, "incidentCount", incidentCount)

# attributes from prior widgets created in sections above.
setattr(window, "incidentsCommandListbox", incidentsCommandListbox)
setattr(window, "scale_value", scale_value)
setattr(window, "dateCreatedText", dateCreatedText)
setattr(window, "dateOnSiteText", dateOnSiteText)
setattr(window, "supervisorNameText", supervisorNameText)
setattr(window, "recordIDText", recordIDText)
setattr(window, "crewIDText", crewIDText)

def onEsc(event):
    sys.exit()

def onClosing():
    window.destroy()

def updateGUI(window):
    # MAIN CODE HERE
    window.update()
    window.after(0, func = lambda: updateGUI(window))

# binds/event handlers
window.bind("<Escape>", onEsc)
window.protocol("WM_DELETE_WINDOW", onClosing)

window.after(0, func = lambda: updateGUI(window))
window.mainloop()
