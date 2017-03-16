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
		#self.load_img = {n:"sand.jpeg", n+1:"silty.jpg",n+2:"clay.jpg",n+3:"rainwater.jpg",n+4:"ice.jpg",n+5:"snowwater.jpg",n+6:"sedimetary.JPG",n+7:"metamorphic.jpg",n+8:"Igneous.jpeg",n+9:"oxides.jpg", n+10:"carbonates.jpg",n+11: "phosphates.jpg",n+12:"sulfides.jpg",n+13:"native_element.jpg", n+14:"silicates.jpg",n+15:"obstacle.jpeg"}
		self.marker =[0,0]
		self.top =0
		self.counter =0

		self.data_value=0
		self.previous_marker=[0,0]
		self.previous_data_value = []
		self.retrieve_data= []
		self.entered_data =[]
		#### Comment when using input function#####
		# self.top=tk.Tk()
		# self.img = ImageTk.PhotoImage(Image.open("image.png"))
		# self.panel =tk.Label (self.top, image = self.img)
		# self.panel.pack(side = "bottom" ,fill ="both",expand = "yes")
		# self.top.title (" The explorer Bot")
		############## end function###################
		rospy.init_node('ID_Sub')
		rospy.Subscriber("Estimated_marker", Marker, self.Callback)



		################## verified Input function#####################33
		
		self.master = tk.Tk()
		for var in range (0,17):
			Marker_cordinates= "Marker_cordinates_" + str((var/2+1))
			tk.Label(self.master, text="Number_of_marker").grid(row=0)
			if (var%2 != 0):
				tk.Label(self.master, text=Marker_cordinates).grid(row=var)
			if (var<16):
				tk.Label(self.master, text="Marker_ID").grid(row=var+1)
			
			self.entry_level= "entry_level" + str(var)
			self.entry_level = tk.Entry(self.master)	
			self.entry_level.grid(row=var, column=1)
			self.retrieve_data.append(self.entry_level)			

		tk.Button(self.master, text='Quit', command=self.gui_call).grid(row=17, column=1, sticky=tk.W, pady=4)
		tk.Button(self.master, text='Enter to Code', command=self.get_data).grid(row=17, column=2, sticky=tk.W, pady=4)
		self.master.title (" Enter Inputs")
		self.master.mainloop()

		self.top=tk.Tk()
		self.img = ImageTk.PhotoImage(Image.open("image_with_lable.png"))

		self.panel =tk.Label(image = self.img)
		self.panel.pack()
		self.top.title (" The explorer Bot")
		
		############################ end Input Function##############################################
	def gui_call(self):
		self.master.quit()
		self.master.destroy()

	def get_data(self):
		# for var in range(0,17):
		# print self.retrieve_data[0].get()
		# print "Number_of_markers: " + str(self.retrieve_data[0].get())
		for var in range(0,17):
			self.entered_data.append(self.retrieve_data[var].get())
		print self.entered_data
		self.eb ={n:"Sandy",n+1: "Clay",n+2: "Slity",n+3:"Rain Water",n+4: "Ice",n+5: "Snow Water",n+6:"Sedimentry",n+7: "Metamorphic",n+8: "Igneous",n+9:"Oxides",n+10: "Carbonates",n+11: "Phosphates",n+12:"Sulfides",n+13: "Native Element",n+14: "Silicates"}
		self.SOI_list_enter ={self.entered_data[2]:[self.entered_data[1]],self.entered_data[4]:[self.entered_data[3]],self.entered_data[6]:[self.entered_data[5]],self.entered_data[8]:[self.entered_data[7]],self.entered_data[10]:[self.entered_data[9]],self.entered_data[12]:[self.entered_data[11]],self.entered_data[14]:[self.entered_data[13]],self.entered_data[16]:[self.entered_data[15]] }
		print self.SOI_list_enter
		self.gui_function()			

	def Callback(self,data):
	    #marker =[n,n+1,n+2,n+3,n+4,n+5,n+6,n+7,n+8,n+9,n+10,n+11,n+12,n+13,n+14,n+15,n+16,n+17,n+18,n+19,n+20]
	    self.data_value = data.id
	    # self.gui_list = self.SOI_list[self.data_value]
	    # self.marker =self.SOI_list[self.data_value]
	    
	    if (self.previous_marker != self.data_value):
	    	self.gui_function()
	    	self.previous_marker = self.data_value
     
	def gui_function(self):
		try:
			
			#self.panel =tk.Label (self.top, image = self.img)
			#self.panel.pack(side = "bottom" ,fill ="both",expand = "yes")
			self.load_img = {n: "sand.jpeg", n+1:"silty.jpg",n+2:"clay.jpg",n+3:"rainwater.jpg",n+4:"ice.jpg",n+5:"snowwater.jpg",n+6:"sedimetary.JPG",n+7:"metamorphic.jpg",n+8:"Igneous.jpeg", n+9:"oxides.jpg", n+10:"carbonates.jpg", n+11:"phosphates.jpg",n+12:"sulfides.jpg",n+13:"native_element.jpg",n+14: "silicates.jpg",n+20:"obstacle_Found.png"}
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

			########### Update With Loop #################3
			
			# for x in xrange(0,16):
			# 	self.value ="img" + str (x)
			# 	self.panel_num = "panel" +str (x)
			# 	self.load_image = self.load_img[x]
			# 	self.value = Image.open(self.load_image)
			# 	self.value = self.value.resize((65,65), Image.ANTIALIAS)
			# 	self.value = ImageTk.PhotoImage(self.value)
			# 	self.panel_num =tk.Label (self.top, image = self.value)
			# 	self.panel_num.pack()
			# 	self.panel_num.place (x = 68 + (5 *x)  , y = 68 + (5*x))

			###################### End Update With Loop #############################
			print self.entered_data[2:]
			print self.data_value
			if (str(self.data_value) ==self.entered_data[2]):

				cordinate = self.SOI_list_enter[str(self.data_value)]
				cordinate = cordinate[0]
				# print cordinate[0]
				if (200<=self.data_value >=216):
					self.load_image1 = self.load_img[220]
					self.value1 = Image.open(self.load_image1)
				else:
					self.load_image1 = self.load_img[self.data_value]
					self.value1 = Image.open(self.load_image1)
				self.value1 = self.value1.resize((65,65), Image.ANTIALIAS)
				self.value1 = ImageTk.PhotoImage(self.value1)
				self.panel_num1 =tk.Label (self.top, image = self.value1)
				self.panel_num1.pack()
				self.panel_num1.place (x = 68 + (73*int(cordinate[0]))   , y = 68 + (73 * (6- (int(cordinate[2])))))    #removed X
			
			if (str(self.data_value) ==self.entered_data[4]):

				cordinate = self.SOI_list_enter[str(self.data_value)]
				cordinate = cordinate[0]
				if (200<=self.data_value >=216):
					self.load_image2 = self.load_img[220]
					self.value2 = Image.open(self.load_image2)
				else:
					self.load_image2 = self.load_img[self.data_value]
					self.value2 = Image.open(self.load_image2)
				self.value2 = self.value2.resize((65,65), Image.ANTIALIAS)
				self.value2 = ImageTk.PhotoImage(self.value2)	
				self.panel_num2 =tk.Label (self.top, image = self.value2)
				self.panel_num2.pack()				
				self.panel_num2.place (x = 68 + (73*int(cordinate[0]))   , y = 68 + (73 * (6- (int(cordinate[2])))))
			if (str(self.data_value) ==self.entered_data[6]):

				cordinate = self.SOI_list_enter[str(self.data_value)]
				cordinate = cordinate[0]
				# print cordinate[0]
				if (200<=self.data_value >=216):
					self.load_image3 = self.load_img[220]
					self.value3 = Image.open(self.load_image3)
				else:
					self.load_image3 = self.load_img[self.data_value]
					self.value3 = Image.open(self.load_image3)
				self.value3 = self.value3.resize((65,65), Image.ANTIALIAS)
				self.value3 = ImageTk.PhotoImage(self.value3)
				self.panel_num3 =tk.Label (self.top, image = self.value3)
				self.panel_num3.pack()
				self.panel_num3.place (x = 68 + (73*int(cordinate[0]))   , y = 68 + (73 * (6- (int(cordinate[2])))))    #removed X
			
			if (str(self.data_value) ==self.entered_data[8]):

				cordinate = self.SOI_list_enter[str(self.data_value)]
				cordinate = cordinate[0]
				# print cordinate[0]
				if (200<=self.data_value >=216):
					self.load_image4 = self.load_img[220]
					self.value4 = Image.open(self.load_image4)
				else:
					self.load_image4 = self.load_img[self.data_value]
					self.value4 = Image.open(self.load_image4)
				self.value4 = self.value4.resize((65,65), Image.ANTIALIAS)
				self.value4 = ImageTk.PhotoImage(self.value4)
				self.panel_num4 =tk.Label (self.top, image = self.value4)
				self.panel_num4.pack()
				self.panel_num4.place (x = 68 + (73*int(cordinate[0]))   , y = 68 + (73 * (6- (int(cordinate[2])))))    #removed X
			
			if (str(self.data_value) ==self.entered_data[10]):

				cordinate = self.SOI_list_enter[str(self.data_value)]
				cordinate = cordinate[0]
				# print cordinate[0]
				if (200<=self.data_value >=216):
					self.load_image5 = self.load_img[220]
					self.value5 = Image.open(self.load_image5)
				else:
					self.load_image5 = self.load_img[self.data_value]
					self.value5 = Image.open(self.load_image5)
				self.value5 = self.value5.resize((65,65), Image.ANTIALIAS)
				self.value5 = ImageTk.PhotoImage(self.value5)
				self.panel_num5 =tk.Label (self.top, image = self.value5)
				self.panel_num5.pack()
				self.panel_num5.place (x = 68 + (73*int(cordinate[0]))   , y = 68 + (73 * (6- (int(cordinate[2])))))    #removed X
			
			if (str(self.data_value) ==self.entered_data[12]):

				cordinate = self.SOI_list_enter[str(self.data_value)]
				cordinate = cordinate[0]
				# print cordinate[0]
				if (200<=self.data_value >=216):
					self.load_image6 = self.load_img[220]
					self.value6 = Image.open(self.load_image6)
				else:
					self.load_image6 = self.load_img[self.data_value]
					self.value6 = Image.open(self.load_image6)
				self.value6 = self.value6.resize((65,65), Image.ANTIALIAS)
				self.value6 = ImageTk.PhotoImage(self.value6)
				self.panel_num6 =tk.Label (self.top, image = self.value6)
				self.panel_num6.pack()
				self.panel_num6.place (x = 68 + (73*int(cordinate[0]))   , y = 68 + (73 * (6- (int(cordinate[2])))))    #removed X
			
			if (str(self.data_value) ==self.entered_data[14]):

				cordinate = self.SOI_list_enter[str(self.data_value)]
				cordinate = cordinate[0]
				# print cordinate[0]
				if (200<=self.data_value >=216):
					self.load_image7 = self.load_img[220]
					self.value7 = Image.open(self.load_image7)
				else:
					self.load_image7 = self.load_img[self.data_value]
					self.value7 = Image.open(self.load_image7)
				self.value7 = self.value7.resize((65,65), Image.ANTIALIAS)
				self.value7 = ImageTk.PhotoImage(self.value7)
				self.panel_num7 =tk.Label (self.top, image = self.value7)
				self.panel_num7.pack()
				self.panel_num7.place (x = 68 + (73*int(cordinate[0]))   , y = 68 + (73 * (6- (int(cordinate[2])))))    #removed X
			
			if (str(self.data_value) ==self.entered_data[16]):

				cordinate = self.SOI_list_enter[str(self.data_value)]
				cordinate = cordinate[0]
				# print cordinate[0]
				if (200<=self.data_value >=216):
					self.load_image8 = self.load_img[220]
					self.value8 = Image.open(self.load_image8)
				else:
					self.load_image8 = self.load_img[self.data_value]
					self.value8 = Image.open(self.load_image8)
				self.value8 = self.value8.resize((65,65), Image.ANTIALIAS)
				self.value8 = ImageTk.PhotoImage(self.value8)
				self.panel_num8 =tk.Label (self.top, image = self.value8)
				self.panel_num8.pack()
				self.panel_num8.place (x = 68 + (73*int(cordinate[0]))   , y = 68 + (73 * (6- (int(cordinate[2])))))    #removed X
			
			self.top.update()			
			self.top.resizable(0,0)
			try:
				rospy.loginfo("Marker ID %s : %s", self.data_value, self.SOI_list[self.data_value])
			except KeyError:
				rospy.loginfo("Marker ID %s : %s", self.data_value, "No record Found of this marker")
		except:
			pass
		# self.top.mainloop()

if __name__ == '__main__':
    gui_fun = GUI_INIT()
    # gui_fun.gui_function()
    # gui_fun.top.resizable(0,0)
    tk.mainloop()
    # gui_fun.top.resizable(0,0)
    rospy.spin()
