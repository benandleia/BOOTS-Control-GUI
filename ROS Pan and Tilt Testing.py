# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 17:01:18 2023

@author: Acoustics_NDST
"""

"""
Testing Comms with the ROS Pan and Tilt Unit (PT-10)

This is an RS-485 device, connected to the subsea MOXA at 192.168.3.53, port 4.

First node (A) is rotation left to right, second node (B) is tilting up/down

Original commands locked the speed to 5 degrees per second in both axes. Braking is set to
engage immediately after the button is released. Stronger braking is engaged on the
the left/right axis (064) as compared to the up/down axis (032).

Current Command set:
    
A<010
A>010
B>010
B<010
As064
Bs032

"""

import socket
from time import sleep
import pygame

#Initialize F310 joystick and display_init() for pygame's event pump function.
pygame.display.init()
pygame.joystick.init()

try:
    F310 = pygame.joystick.Joystick(0)
    F310.init()
except:
    pass

#Start the event pump function
#Deadband values are less than ABS(0.10), scale is 1 to -1, for both axes.

while True:
    pygame.event.pump()
    left_right = F310.get_axis(2) #Negative values are left
    up_down = F310.get_axis(3) #Negative values are up
    print(f'Left_Right {left_right}')
    print(f'Up_Down {up_down}')
    sleep(1)

#set up normal socket type for TCP/IP comms
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the socket using desired IP and Port
IP_ADDRESS = "192.168.3.53"
PORT = 4004 #Local Port for MOXA Port 4, which is the Pan and Tilt
sock.connect((IP_ADDRESS, PORT))
sock.settimeout(5)

"""
Pan Left = A>010
Pan_Right = A<010
Pan_Brake = As032
Tilt Up = B<010
Tilt Down = B>010
Tilt Brake = Bs064

"""
#Movement Commands

pan_left_command = [b'A', b'>',b'0',b'1',b'0']
pan_right_command = [b'A',b'<',b'0',b'1',b'0']
pan_brake_command = [b'A',b's',b'0',b'3',b'2']
tilt_up_command = [b'B',b'<',b'0',b'1',b'0']
tilt_down_command = [b'B',b'>',b'0',b'1',b'0']
tilt_brake_command = [b'B',b's',b'0',b'6',b'4']

#Empty List to hold the command echo string, sent back by the Pan and Tilt unit
move_command_resp = []

while True:
    pygame.event.pump()
    pan_val = F310.get_axis(2)
    tilt_val = F310.get_axis(3)
    #Negative values on the left/right joystick when stick pushed to the left
    if pan_val < -0.1 : 
        for i in pan_left_command:
            sock.sendall(i)
            move_command_resp.append(sock.recv(4))
        print(move_command_resp)
        move_command_resp.clear()
    #Positive values on the left/right joystick when stick pushed to the right
    elif pan_val > 0.1 :
        for i in pan_right_command:
            sock.sendall(i)
            move_command_resp.append(sock.recv(4))
        print(move_command_resp)
        move_command_resp.clear()
    elif tilt_val < -0.1 :
        for i in pan_right_command:
            sock.sendall(i)
            move_command_resp.append(sock.recv(4))
        print(move_command_resp)
        move_command_resp.clear()
    elif tilt_val > 0.1 :
        for i in pan_right_command:
            sock.sendall(i)
            move_command_resp.append(sock.recv(4))
        print(move_command_resp)
        move_command_resp.clear()

#Close the socket
sock.close()