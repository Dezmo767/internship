#!/usr/bin/env python3
import socket
import threading
import sys
import getopt
import subprocess



'''
# TCP Client
target_host = "www.google.lu"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the Client
client.connect((target_host, target_port))

# Send some Data
client.send("GET / HTTP/1.1\r\nHost: google.lu\r\n\r\n")

# Receive some Data
response = client.recv(4096)

print(response)

###############

# UDP Client
target_host = "127.0.0.1"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some Data
client.sendto("AAABBBCCC",(target_host, target_port))

# Receive some Data
data, addr = client.recvfrom(4096)

print(data)
############

# TCP Server

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

# this is our client-handeling thread
def handle_client(client_socket):
	
	# Print out what the Client sends
	request = client.socket.recv(1024)
	
	print "[*] Received: %s" % request
	
	# Send back a packet
	client_socket.send("ACK!")
	client_socket.close()
	
while True:
	
	client,addr = server.accept()
	print "[*] Accept connection From %s:%d" % (addr[0],addr[1])
		
	# Spin up our client thread to handle incoming Data
	client_handler = threading.Thread(target=handle_client,args=(client,))
	client_handler.start()

#######

import scapy
from scapy.all import *

# our packet callback

def packet_callback(packet):
	
	if packet[TCP].payload:
		mail_packet = str(packet[TCP].payload)
		if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
			print "[*] Server: %s" % packet[IP].dst
			print "[*] %s" % packet[TCP].payload

#fire up our sniffer

sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",prn=packet_¬callback,store=0)
'''
		
		














