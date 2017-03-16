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
		####################### Input Function################
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

		######################### End Input Function############################
		self.rate =10
		self.gui_list = [0,0]
		self.eb ={n:"Sandy",n+1: "Clay",n+2: "Slity",n+3:"Rain Water",n+4: "Ice",n+5: "Snow Water",n+6:"Sedimentry",n+7: "Metamorphic",n+8: "Igneous",n+9:"Oxides",n+10: "Carbonates",n+11: "Phosphates",n+12:"Sulfides",n+13: "Native Element",n+14: "Silicates"}
		self.SOI_list ={n:[1,5],n+1: [0,0],n+2: [0,0],n+3:[0,0],n+4: [0,0],n+5: [4,6],n+6:[0,0],n+7: [0,0],n+8: [0,0],n+9:[5,2],n+10: [0,0],n+11: [0,0],n+12:[6,4],n+13: [5,0],n+14: [0,0], n+17: [2,3], n+19: [3,4], n+20: [1,1]}
		self.load_img = {n:"sand.jpeg", n+1:"silty.jpg",n+2:"clay.jpg",n+3:"rainwater.jpg",n+4:"ice.jpg",n+5:"snowwater.jpg",n+6:"sedimetary.JPG",n+7:"metamorphic.jpg",n+8:"Igneous.jpeg",n+9:"oxides.jpg", n+10:"carbonates.jpg",n+11: "phosphates.jpg",n+12:"sulfides.jpg",n+13:"native_element.jpg", n+14:"silicates.jpg",n+15:"obstacle.jpeg"}
		self.marker =[0,0]
		self.top =0
		self.counter =0
		self.data_value=0
		self.previous_marker=[0,0]
		self.previous_data_value = []
		self.top=tk.Tk()
		self.img = ImageTk.PhotoImage(Image.open("image.png"))
		self.panel =tk.Label (self.top, image = self.img)
		self.panel.pack(side = "bottom" ,fill ="both",expand = "yes")
		rospy.init_node('ID_Sub')
		rospy.Subscriber("Estimated_marker", Marker, self.Callback)

		def Callback(self,data):
	    #marker =[n,n+1,n+2,n+3,n+4,n+5,n+6,n+7,n+8,n+9,n+10,n+11,n+12,n+13,n+14,n+15,n+16,n+17,n+18,n+19,n+20]
		    self.gui_list = self.SOI_list[data.id]
		    self.marker =self.SOI_list[data.id]
		    self.data_value = data.id
		    if (self.previous_marker != self.data_value):
		    	self.gui_function()
		    	self.previous_marker = self.data_value






if __name__ == '__main__':
    gui_fun = GUI_INIT()
    #gui_fun.gui_function()
    # gui_fun.top.resizable(0,0)
    tk.mainloop()
    rospy.spin()
