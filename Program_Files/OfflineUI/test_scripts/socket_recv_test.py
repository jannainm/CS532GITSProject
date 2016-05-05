'''
Created on May 2, 2016
@author: jannainm
'''
import socket

recv_data = ''

# fd = open('logging', 'w')
# fd.write(recv_data)
# fd.close()

HOST = "localhost"
PORT = 65000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', PORT))
server.listen(5)

def writeToFd():
    fd = open('logging', 'w')
    fd.write(recv_data)
    fd.close()

while True:
    client, address = server.accept()
    print('Connection from: ', address)
    while(1):
        recv_data = client.recv(512)
        if not recv_data:
            break
        print 'RECIEVED:', recv_data
        writeToFd()
    client.shutdown(socket.SHUT_WR)
    client.close()
    
    ##
    ## ADD A STRING SEPERATOR HERE TO SEPERATE DATA ELEMENTS BY ,
    ##