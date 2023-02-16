# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 21:21:04 2023

@author: SnowBe
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:07:12 2020

@author: Acoustics_NDST
"""

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
#import pygame
#import ncd_indstrial_relays as ncd

#######################################################################################################################################
###                     Main GUI class
#######################################################################################################################################


    
class MainWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title("BOOTS Control V2.0")
        #Overwrite default shutdown behaviour
        self.parent.protocol("WM_DELETE_WINDOW" , self.CloseProgram)
        self.parent.geometry("1000x800")
       
    
        
        #Label for Relay Controls
        tk.Label(self, text = "Relay Controls").grid(row=0, column = 0, pady = 10, padx = 5)
        
        
        #Relay buttons for Bank 1 (main ProXR relay card)
        tk.Label(self, text = "MiniZeus").grid(row = 1, column =0, pady = 5)
        self.RB1_1_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB1_1)
        self.RB1_1_toggle.grid(row = 1, column =1, padx = 5, pady = 5)
        
        tk.Label(self, text = "RayFin Mk2").grid(row = 2, column =0, pady = 5)
        self.RB1_2_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB1_2)
        self.RB1_2_toggle.grid(row = 2, column =1, padx = 5, pady = 5)
        
        tk.Label(self, text = "CTD").grid(row = 3, column =0, pady = 5)        
        self.RB1_3_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB1_3)
        self.RB1_3_toggle.grid(row = 3, column =1, padx = 5, pady = 5)
        
        tk.Label(self, text = "Responder").grid(row = 4, column =0, pady = 5)        
        self.RB1_4_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB1_4)
        self.RB1_4_toggle.grid(row = 4, column =1, padx = 5, pady = 5)
        
        tk.Label(self, text = "Pan & Tilt/Depth").grid(row = 5, column =0, pady = 5)        
        self.RB1_5_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB1_5)
        self.RB1_5_toggle.grid(row = 5, column =1, padx = 5, pady = 5)
        
        tk.Label(self, text = "Not Connected").grid(row = 6, column =0, pady = 5)        
        self.RB1_6_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB1_6)
        self.RB1_6_toggle.grid(row = 6, column =1, padx = 5, pady = 5)
        
        tk.Label(self, text = "Tritech/SD Cam").grid(row = 7, column =0, pady = 5)        
        self.RB1_7_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB1_7)
        self.RB1_7_toggle.grid(row = 7, column =1, padx = 5, pady = 5)
        
        tk.Label(self, text = "Sonar").grid(row = 8, column =0, pady = 5)        
        self.RB1_8_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB1_8)
        self.RB1_8_toggle.grid(row = 8, column =1, padx = 5, pady = 5)
        
        
        #Relay buttons for Bank 4 (ProXR relay expansion card)
        
        tk.Label(self, text = "Altimeter").grid(row = 1, column =2, pady = 5)         
        self.RB4_1_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB4_1)
        self.RB4_1_toggle.grid(row = 1, column =3, padx = 5, pady = 5)
        
        tk.Label(self, text = "Sphere Lights").grid(row = 2, column =2, pady = 5)         
        self.RB4_2_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB4_2)
        self.RB4_2_toggle.grid(row = 2, column =3, padx = 5, pady = 5)
        
        tk.Label(self, text = "Lasers").grid(row = 3, column =2, pady = 5)       
        self.RB4_3_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB4_3)
        self.RB4_3_toggle.grid(row = 3, column =3, padx = 5, pady = 5)
        
        tk.Label(self, text = "GoPro Trickle Charge").grid(row = 4, column =2, pady = 5)        
        self.RB4_4_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB4_4)
        self.RB4_4_toggle.grid(row = 4, column =3, padx = 5, pady = 5)
        
        tk.Label(self, text = "Port ROS LED Light").grid(row = 5, column =2, pady = 5)        
        self.RB4_5_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB4_5)
        self.RB4_5_toggle.grid(row = 5, column =3, padx = 5, pady = 5)
        
        tk.Label(self, text = "Stbd ROS LED Light").grid(row = 6, column =2, pady = 5)        
        self.RB4_6_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB4_6)
        self.RB4_6_toggle.grid(row = 6, column =3, padx = 5, pady = 5)
        
        tk.Label(self, text = "Port HID Light").grid(row = 7, column =2, pady = 5)           
        self.RB4_7_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB4_7)
        self.RB4_7_toggle.grid(row = 7, column =3, padx = 5, pady = 5)
        
        tk.Label(self, text = "Stbd HID Light").grid(row = 8, column =2, pady = 5)          
        self.RB4_8_toggle = tk.Button(self, text = "OFF", bg = 'grey', command=self.RB4_8)
        self.RB4_8_toggle.grid(row = 8, column =3, padx = 5, pady = 5)


        #Alarms Pane
        tk.Label(self, text = 'Alarms').grid(row = 9, column = 0, pady = 70)        
        
        
    #Function to check all relay status at start up.
    def RelayStatus(self):
        for i in 
        
    #Custom quit function, close the pigpiod instance when terminating the program.
    def CloseProgram(self):
        self.parent.destroy() #Kill Tk root instance.
        
        
        
###############################################################################################################
##                              BUTTONS SPECIFIC FUNCTIONS                                                  ##
###############################################################################################################

    #Relay Bank 1
    def RB1_1(self):
        if self.RB1_1_toggle["bg"] == 'grey':
            self.RB1_1_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB1_1_toggle.configure(bg = "grey", text = "OFF")             
    def RB1_2(self):
        if self.RB1_2_toggle["bg"] == 'grey':
            self.RB1_2_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB1_2_toggle.configure(bg = "grey", text = "OFF")   
    def RB1_3(self):
        if self.RB1_3_toggle["bg"] == 'grey':
            self.RB1_3_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB1_3_toggle.configure(bg = "grey", text = "OFF")           
    def RB1_4(self):
        if self.RB1_4_toggle["bg"] == 'grey':
            self.RB1_4_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB1_4_toggle.configure(bg = "grey", text = "OFF")           
    def RB1_5(self):
        if self.RB1_5_toggle["bg"] == 'grey':
            self.RB1_5_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB1_5_toggle.configure(bg = "grey", text = "OFF")   
            
    def RB1_6(self):
        if self.RB1_6_toggle["bg"] == 'grey':
            self.RB1_6_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB1_6_toggle.configure(bg = "grey", text = "OFF")   
    def RB1_7(self):
        if self.RB1_7_toggle["bg"] == 'grey':
            self.RB1_7_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB1_7_toggle.configure(bg = "grey", text = "OFF")           
    def RB1_8(self):
        if self.RB1_8_toggle["bg"] == 'grey':
            self.RB1_8_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB1_8_toggle.configure(bg = "grey", text = "OFF")              
    
    #Relay bank 4
    def RB4_1(self):
        if self.RB4_1_toggle["bg"] == 'grey':
            self.RB4_1_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB4_1_toggle.configure(bg = "grey", text = "OFF")              
    def RB4_2(self):
        if self.RB4_2_toggle["bg"] == 'grey':
            self.RB4_2_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB4_2_toggle.configure(bg = "grey", text = "OFF")   
    def RB4_3(self):
        if self.RB4_3_toggle["bg"] == 'grey':
            self.RB4_3_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB4_3_toggle.configure(bg = "grey", text = "OFF")           
    def RB4_4(self):
        if self.RB4_4_toggle["bg"] == 'grey':
            self.RB4_4_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB4_4_toggle.configure(bg = "grey", text = "OFF")           
    def RB4_5(self):
        if self.RB4_5_toggle["bg"] == 'grey':
            self.RB4_5_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB4_5_toggle.configure(bg = "grey", text = "OFF")               
    def RB4_6(self):
        if self.RB4_6_toggle["bg"] == 'grey':
            self.RB4_6_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB4_6_toggle.configure(bg = "grey", text = "OFF")   
    def RB4_7(self):
        if self.RB4_7_toggle["bg"] == 'grey':
            self.RB4_7_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB4_7_toggle.configure(bg = "grey", text = "OFF")           
    def RB4_8(self):
        if self.RB4_8_toggle["bg"] == 'grey':
            self.RB4_8_toggle.configure(bg = "green", text = "ON")
        else:
            self.RB4_8_toggle.configure(bg = "grey", text = "OFF")             
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

##############################################CALL THE MAINLOOP##################################################
        
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).grid(row = 0, column =0)
    root.mainloop()
        