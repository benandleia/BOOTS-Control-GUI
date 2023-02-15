# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:05:41 2023

@author: Acoustics_NDST
"""

"""
Testing BOOTS relay controls, relay status, and reading from ADC

"""

#import the pyserial module
import socket
import ncd_industrial_relay




#set up your socket with the desired settings.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#instantiate the board object and pass it the network socket
board1 = ncd_industrial_relay.Relay_Controller(sock)
#connect the socket using desired IP and Port
IP_ADDRESS = "192.168.3.52"
PORT = 2101 #Default port for the ProXR relays.
sock.connect((IP_ADDRESS, PORT))
sock.settimeout(.5)

"""
Physical Relay Mapping:

Relay Board 1 = RB1, Main Board. This is bank 1.
Relay Board 2 = RB2, Daughter Board. This is bank 4, banks 2 and 3 are the XLR60CLP open collector board.

RB1-1 = MiniZeus Hd Camera
RB1-2 = RayFin Still Camera
RB1-3 = CTD Power
RB1-4 = Responder Trickle Charge
RB1-5 =
RB1-6 = 
RB1-7 =
RB1-8 =

RB2-1 = Altimeter
RB2-2 =
RB2-3 =
RB2-4 = Lasers
RB2-5 =
RB2-6 =
RB2-7 =
RB2-8 =

Physical Analog to Digital Converter Mapping (from DTEC ground fault monitoring board):
    
ADC1 =
ADC2 =
ADC3 =
ADC4 =
ADC5 =
ADC6 =
ADC7 =
ADC8 =
    
"""

#first argument is the relay number, second argument is the relay bank number.

board1.turn_on_relay_by_bank(2, 1)
board1.turn_off_relay_by_bank(2, 1)

board1.turn_on_relay_by_bank(1, 2)

#pass these methods a number between 1 and 512 to get the current status of the relay
stat_1 = board1.get_relay_status_by_index(1)
stat_2 = board1.get_relay_status_by_index(2)



stat_3 = board1.get_relay_bank_status(1)



#Function to poll all 8 ADC at once. Returns a list of 8 values, ranging from 0 to 1023
#TODO scale ADC values to range of DTEC board, in ohms.

try:
    adc_all = board1.read_all_ad10()
except:
    print ('The ADC read command failed due to a socket timeout. Most likely your board does not have AD Inputs')

#close the interface, not necessary here but you may need to in your application
sock.close()




#you can renew or replace your communication interface with new settings if desired.
#serial_port = serial.Serial('COM27', baudrate=115200, bytesize=8, stopbits=1, timeout=.5)
#you can update this serial port by using the following method and passing the new combus
#this would allow you to switch between two interfaces on a fusion board for instance.
#Could be used if the network interface goes down and you need to communicate to it via a USB port.
#board1.renew_replace_interface(serial_port)

#sockets require you to re-instantiate the connection as the OS wipes the connection data on close.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP_ADDRESS, PORT))
sock.settimeout(.5)

board1.renew_replace_interface(sock)
