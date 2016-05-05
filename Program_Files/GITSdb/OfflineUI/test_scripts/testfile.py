'''
Created on May 3, 2016

@author: jannainm
'''
fd = open("newfile.txt", "w")
fd.write("hello world in the new file")
fd.write("and another line")
fd.close()
