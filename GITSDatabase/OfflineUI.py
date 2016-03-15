'''
import Tkinter

window = Tkinter.Tk()

labelNameList = ["Date:", "Time:", "Name:", "Enter:"]

label1 = Tkinter.Label(window, text = labelNameList[0], font = "TkDefaultFont", width = 5)
label1.grid(row = 0, column = 0)

text1 = Tkinter.Text(window, height = 1, width = 10)
text1.grid(row = 0, column = 1)

label2 = Tkinter.Label(window, text = labelNameList[1], font = "TkDefaultFont")
label2.grid(row = 1, column = 0)

text2 = Tkinter.Text(window, height = 1, width = 10)
text2.grid(row = 1, column = 1)

label3 = Tkinter.Label(window, text = labelNameList[2], font = "TkDefaultFont")
label3.grid(row = 2, column = 0)

text3 = Tkinter.Text(window, height = 1, width = 10)
text3.grid(row = 2, column = 1)

label4 = Tkinter.Label(window, text = labelNameList[3], font = "TkDefaultFont")
label4.grid(row = 3, column = 0)

output = Tkinter.Text(window, height = 10, width = 25)
output.grid(row = 4, column = 1)

enterButton = Tkinter.Button(window, text = "Enter", command = lambda: writeInfoToOutput())
enterButton.grid(row = 3, column = 1)

def writeInfoToOutput():
    output.insert("insert", labelNameList[0] + " " + text1.get("1.0", "end"))
    output.insert("insert", labelNameList[1] + " " + text2.get("1.0", "end"))
    output.insert("insert", labelNameList[2] + " " + text3.get("1.0", "end"))

window.mainloop()
'''

'''
Created on Mar 8, 2016

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

import Tkinter
import ttk

newGeometry = "640x480"
windowHeight = 640
windowWidth = 480


window = Tkinter.Tk()
window.geometry(newGeometry)

'''
labelNameList = ["Date:", "Time:", "Name:", "Enter:"]

label1 = Tkinter.Label(window, text = labelNameList[0], font = "TkDefaultFont", width = 5)
label1.grid(row = 0, column = 0)

text1 = Tkinter.Text(window, height = 1, width = 10)
text1.grid(row = 0, column = 1)

label2 = Tkinter.Label(window, text = labelNameList[1], font = "TkDefaultFont")
label2.grid(row = 1, column = 0)

text2 = Tkinter.Text(window, height = 1, width = 10)
text2.grid(row = 1, column = 1)

label3 = Tkinter.Label(window, text = labelNameList[2], font = "TkDefaultFont")
label3.grid(row = 2, column = 0)

text3 = Tkinter.Text(window, height = 1, width = 10)
text3.grid(row = 2, column = 1)

label4 = Tkinter.Label(window, text = labelNameList[3], font = "TkDefaultFont")
label4.grid(row = 3, column = 0)

output = Tkinter.Text(window, height = 10, width = 25)
output.grid(row = 4, column = 1)

enterButton = Tkinter.Button(window, text = "Enter", command = lambda: writeInfoToOutput())
enterButton.grid(row = 3, column = 1)

def writeInfoToOutput():
    output.insert("insert", labelNameList[0] + " " + text1.get("1.0", "end"))
    output.insert("insert", labelNameList[1] + " " + text2.get("1.0", "end"))
    output.insert("insert", labelNameList[2] + " " + text3.get("1.0", "end"))
'''

# View Incident Record Info & Crew Info
# Record ID
# Date created
# Crew ID
# Supervisor Name
# Date on site
# Scale of cleanup effort--select from pre-defined list

recordIDList = []
dateCreatedList = []
crewIDList = []
supervisorNameList = []
dateOnSiteList = []
scaleOfCleanupList = []

recordIDLabel = Tkinter.Label(window, text = "Record ID:", font = "TkDefaultFont")
recordIDLabel.grid(row = 0, column = 0, sticky = "e")

recordIDText = Tkinter.Text(window, height = 1, width = 10)
recordIDText.grid(row = 0, column = 1, columnspan = 2, sticky = "ew")

dateCreatedLabel = Tkinter.Label(window, text = "Date Created:", font = "TkDefaultFont")
dateCreatedLabel.grid(row = 1, column = 0, sticky = "e")

dateCreatedText = Tkinter.Text(window, height = 1, width = 10)
dateCreatedText.grid(row = 1, column = 1, columnspan = 2, sticky = "ew")

crewIDLabel = Tkinter.Label(window, text = "Crew ID:", font = "TkDefaultFont")
crewIDLabel.grid(row = 2, column = 0, sticky = "e")

crewIDText = Tkinter.Text(window, height = 1, width = 10)
crewIDText.grid(row = 2, column = 1, columnspan = 2, sticky = "ew")

supervisorNameLabel = Tkinter.Label(window, text = "Supervisor Name:", font = "TkDefaultFont")
supervisorNameLabel.grid(row = 3, column = 0, sticky = "e")

supervisorNameText = Tkinter.Text(window, height = 1, width = 10)
supervisorNameText.grid(row = 3, column = 1, columnspan = 2, sticky = "ew")

dateOnSiteLabel = Tkinter.Label(window, text = "Date on Site:", font = "TkDefaultFont")
dateOnSiteLabel.grid(row = 4, column = 0, sticky = "e")

dateOnSiteText = Tkinter.Text(window, height = 1, width = 10)
dateOnSiteText.grid(row = 4, column = 1, columnspan = 2, sticky = "ew")

window.update()

# THIS CAN BE A PRE-ASSIGNED VALUE....MAYBE LABEL NOT BEST
#scaleOfCleanupLabel = Tkinter.Label(window, text = "Scale of Cleanup:", font = "TkDefaultFont")
subFrameBottomHalf = Tkinter.Frame(window)
subFrameBottomHalf.grid(row = windowHeight/2, column = 0)

notebookWidget = ttk.Notebook(subFrameBottomHalf)
notebookWidget.grid(row = 0, column = 0, sticky = "ew")
notebookWidget.add(subFrameBottomHalf, text = "Output")

#outputText = Tkinter.Text(subFrameBottomHalf, height = 10, width = 25)
#outputText.grid(row = 0, column = 3, sticky = "ew")

window.update()
window.mainloop()
window.destroy()
