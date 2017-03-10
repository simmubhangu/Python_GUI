#!/usr/bin/env python
import rospy
import time
from visualization_msgs.msg import Marker
import Tkinter as tk
from PIL import ImageTk
import Image
n =200

class GUI_INIT:


	def __init__(self):
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
     
	def gui_function(self):

		#self.panel =tk.Label (self.top, image = self.img)
		#self.panel.pack(side = "bottom" ,fill ="both",expand = "yes")
		self.load_img = ["sand.jpeg", "silty.jpg","clay.jpg","rainwater.jpg","ice.jpg","snowwater.jpg","sedimetary.JPG","metamorphic.jpg","Igneous.jpeg","oxides.jpg", "carbonates.jpg", "phosphates.jpg","sulfides.jpg","native_element.jpg", "silicates.jpg","obstacle.jpeg"]
		#print self.data_value
		############orginal function###################

		# self.previous_data_value.append(self.data_value)
		# for x in range (0,len(self.previous_data_value)):
		# 	print self.previous_data_value

		# 	cordinate = self.SOI_list[self.previous_data_value[x]]
		# 	self.load_image = "load_image" + str (self.previous_data_value[x])
		# 	self.value ="value" + str (self.previous_data_value[x])
		# 	self.panel_num = "panel_num" + str(self.previous_data_value[x])

		# 	self.load_image = self.load_img[self.previous_data_value[x]]
		# 	self.value = Image.open(self.load_image)
		# 	self.value = self.value.resize((65,65), Image.ANTIALIAS)
		# 	self.value = ImageTk.PhotoImage(self.value)
		# 	self.panel_num =tk.Label (self.top, image = self.value)
		# 	self.panel_num.pack()
		# 	self.panel_num.place (x = (68 + 73 * int(cordinate[0]))   , y = (68 + 73 * int(cordinate[1])))

		######################### original function end ####################33

		#self.top.update()

		for x in xrange(0,16):
			self.value ="img" + str (x)
			self.panel_num = "panel" +str (x)
			self.load_image = self.load_img[x]
			self.value = Image.open(self.load_image)
			self.value = self.value.resize((65,65), Image.ANTIALIAS)
			self.value = ImageTk.PhotoImage(self.value)
			self.panel_num =tk.Label (self.top, image = self.value)
			self.panel_num.pack()
			self.panel_num.place (x = 68 + (5 *x)  , y = 68 + (5*x))


		
		self.top.title (" The explorer Bot")
		self.top.resizable(0,0)
		try:
			rospy.loginfo("Marker ID %s : %s", self.data_value, self.SOI_list[self.data_value])
		except KeyError:
			rospy.loginfo("Marker ID %s : %s", self.data_value, "No record Found of this marker")

if __name__ == '__main__':
    gui_fun = GUI_INIT()
    #gui_fun.gui_function()
    gui_fun.top.resizable(0,0)
    gui_fun.top.mainloop()
    rospy.spin()
