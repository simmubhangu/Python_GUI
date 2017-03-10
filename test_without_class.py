#!/usr/bin/env python
import rospy
import time
from visualization_msgs.msg import Marker
import Tkinter as tk
from PIL import ImageTk
import Image
n =200


rate =10
gui_list = [0,0]
eb ={n:"Sandy",n+1: "Clay",n+2: "Slity",n+3:"Rain Water",n+4: "Ice",n+5: "Snow Water",n+6:"Sedimentry",n+7: "Metamorphic",n+8: "Igneous",n+9:"Oxides",n+10: "Carbonates",n+11: "Phosphates",n+12:"Sulfides",n+13: "Native Element",n+14: "Silicates"}
SOI_list ={n:[1,5],n+1: [0,0],n+2: [0,0],n+3:[0,0],n+4: [0,0],n+5: [4,6],n+6:[0,0],n+7: [0,0],n+8: [0,0],n+9:[5,2],n+10: [0,0],n+11: [0,0],n+12:[6,4],n+13: [5,0],n+14: [0,0], n+17: [2,3], n+19: [3,4], n+20: [1,1]}
load_img = {n:"sand.jpeg", n+1:"silty.jpg",n+2:"clay.jpg",n+3:"rainwater.jpg",n+4:"ice.jpg",n+5:"snowwater.jpg",n+6:"sedimetary.JPG",n+7:"metamorphic.jpg",n+8:"Igneous.jpeg",n+9:"oxides.jpg", n+10:"carbonates.jpg",n+11: "phosphates.jpg",n+12:"sulfides.jpg",n+13:"native_element.jpg", n+14:"silicates.jpg",n+15:"obstacle.jpeg"}
marker =[0,0]
top =0
counter =0
data_value=0
previous_marker=[0,0]
previous_data_value = []

# self.top=tk.Tk()
# self.img = ImageTk.PhotoImage(Image.open("image.png"))
# self.panel =tk.Label (self.top, image = self.img)
# self.panel.pack(side = "bottom" ,fill ="both",expand = "yes")
# self.top.title (" The explorer Bot")
rospy.init_node('ID_Sub')
rospy.Subscriber("Estimated_marker", Marker,Callback)



	################## verified Input functio#####################33
def Input_gui():
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
		

	tk.Button(master, text='verify and Quit', command=gui_call).grid(row=17, column=1, sticky=tk.W, pady=4)
	master.title (" Enter Inputs")
	tk.mainloop()
	
	############################ end Input Function##############################################
def gui_call(self):
	master.quit()
	top=tk.Tk()
	img = ImageTk.PhotoImage(Image.open("image.png"))
	panel =tk.Label (top, image = self.img)
	panel.pack(side = "bottom" ,fill ="both",expand = "yes")
	top.title (" The explorer Bot")
	# self.master.quit()
	

def Callback(self,data):
    #marker =[n,n+1,n+2,n+3,n+4,n+5,n+6,n+7,n+8,n+9,n+10,n+11,n+12,n+13,n+14,n+15,n+16,n+17,n+18,n+19,n+20]
    gui_list = SOI_list[data.id]
    marker =SOI_list[data.id]
    data_value = data.id
    if (previous_marker != data_value):
    	gui_function()
    	previous_marker = data_value
 
def gui_function(self):

	#self.panel =tk.Label (self.top, image = self.img)
	#self.panel.pack(side = "bottom" ,fill ="both",expand = "yes")
	load_img = ["sand.jpeg", "silty.jpg","clay.jpg","rainwater.jpg","ice.jpg","snowwater.jpg","sedimetary.JPG","metamorphic.jpg","Igneous.jpeg","oxides.jpg", "carbonates.jpg", "phosphates.jpg","sulfides.jpg","native_element.jpg", "silicates.jpg","obstacle.jpeg"]
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

	top.update()

	for x in xrange(0,16):
		value ="img" + str (x)
		panel_num = "panel" +str (x)
		load_image = load_img[x]
		value = Image.open(load_image)
		value = value.resize((65,65), Image.ANTIALIAS)
		value = ImageTk.PhotoImage(value)
		panel_num =tk.Label (top, image = value)
		panel_num.pack()
		panel_num.place (x = 68 + (5 *x)  , y = 68 + (5*x))


	
	
	top.resizable(0,0)
	try:
		rospy.loginfo("Marker ID %s : %s", data_value, SOI_list[data_value])
	except KeyError:
		rospy.loginfo("Marker ID %s : %s", data_value, "No record Found of this marker")

	top.mainloop()

