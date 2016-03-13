'''
@author: Michael Jannain
'''

'''
GET CODE FROM WINDOWS PC
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