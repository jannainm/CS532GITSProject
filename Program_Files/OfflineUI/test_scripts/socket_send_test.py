'''
Created on May 2, 2016

@author: jannainm
'''
import socket

HOST = "localhost"
PORT = 65000

send_data = "1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print('Sending data to:', HOST)
client.sendall(send_data)
client.shutdown(socket.SHUT_RDWR)
client.close()
