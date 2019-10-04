#!/usr/bin/python3
#
# Nikki Benoit
# Sept 11 2019  09:02:24.224 MST
#
#######################################
# Create a port scanner
#   Bonus: enable multithreading
#######################################

import socket

host = input("Host IPv4 address to scan: ")
ports = [int(x) for x in (input("What port range do you want to scan (Format: 1-2): ").split("-"))]

open_ports = []

for port in range(ports[0], ports[1] + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con = s.connect((host, port))
        open_ports.append(port)

        con.close()
    except:
        pass

if not open_ports:
    print("No ports are open")
else:
    for p in open_ports:
        print('Port: ' + str(p) + ' is open')
