# program name: Assignment4.py
# course: Adv Application Development XLS Group 18 Spring Semester 2025 CO
# student name: Bayden Blackwell
# assignment number: lab#4
# due date: 03/24/2025
# purpose: sends user input to program b and prints the uppercase response
# resources: stackoverflow, youtube, coursenotes, copilot vsc

import socket

# create socket for connecting
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = '127.0.0.1'
server_port = 45000

try:
    # connect to program b
    client_socket.connect((server_ip, server_port))

    # get input from user
    user_input = input("enter a message to send to program b: ")

    # send the message
    client_socket.sendall(user_input.encode())

    # receive and print the response
    response = client_socket.recv(1024).decode()
    print("received from program b:", response)

except ConnectionRefusedError:
    print("connection failed. make sure program b is running.")

finally:
    # close the connection
    client_socket.close()
