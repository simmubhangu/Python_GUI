# from Tkinter import *
import Tkinter as tk
import rospy
import time
from visualization_msgs.msg import Marker
from PIL import ImageTk
import Image
n =200

class GUI_INIT:

		def __init__(self):
			master = tk.Tk()
			for var in range (0,17):
				Marker_cordinates= "Marker_cordinates_" + str((var/2+1))
				tk.Label(master, text="Number_of_marker").grid(row=0)
				if (var%2 != 0):
					tk.Label(master, text=Marker_cordinates).grid(row=var)
				if (var<16):
					tk.Label(master, text="Marker_ID").grid(row=var+1)
				
				entry_level= "entry_level" + str(var)
				entry_level = tk.Entry(master)
				
				entry_level.grid(row=var, column=1)
				

			tk.Button(master, text='verify and Quit', command=master.quit).grid(row=17, column=1, sticky=tk.W, pady=4)
			# Button(master, text='Show', command=show_entry_fields).grid(row=17, column=1, sticky=W, pady=4)
			master.title (" Enter Inputs")

if __name__ == '__main__':
    gui_fun = GUI_INIT()
    #gui_fun.gui_function()
    # gui_fun.top.resizable(0,0)
    tk.mainloop()
    rospy.spin()
