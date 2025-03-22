# program name: Assignment4.py
# course: Adv Application Development XLS Group 18 Spring Semester 2025 CO
# student name: Bayden Blackwell
# assignment number: lab#4
# due date: 03/24/2025
# purpose: sends user input to program b and prints the uppercase response
# resources: stackoverflow, youtube, coursenotes, copilot vsc

import socket

# create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 45000

# bind and start listening
server_socket.bind((host, port))
server_socket.listen(1)

print("program b is waiting for connection...")

# accept connection from program a
conn, addr = server_socket.accept()
print("connected by", addr)

# get message from program a
data = conn.recv(1024).decode()

# convert to uppercase
uppercase_data = data.upper()

# send it back
conn.sendall(uppercase_data.encode())

# close sockets
conn.close()
server_socket.close()
