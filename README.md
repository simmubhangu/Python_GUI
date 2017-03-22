# Python_GUI
This package Contain the Python GUI for Explorer Bot Theme

Package Required:
Tkinter: sudo apt-get install python-tk	
Python Imaging Library(PIL): sudo apt-get install python-PIL

Follow the following instruction
1. Clone the git repository into Laptop/PC and visit to that directory.
2. Run the “final_gui.py” scripts. This script will launch a GUI as shown in Figure-1

***
<p align="center">
  <img src="https://github.com/simubhangu/Python_GUI/blob/master/Readme_images/a.png"> <br>
  <b> Figure-1: GUI to enter Input </b>
</p>

In this GUI enter the detail according to inputs provided in the configuration
1. Number of Markers: Total number of marker present in arena: Maximum will be 8 
2. Marker_Cordinates_*: Coordinates of marker in the arena eg: 1,1 or 2,2 ( Please Don’t add any brackets while entering data)
3. Marker_ID: Marker ID of the object place at respective coordinate. eg: 202, 210 etc.


After entering the input, GUI will appear as shown in Figure-2 
<p align="center">
  <img src="(https://github.com/simubhangu/Python_GUI/blob/master/Readme_images/b.png"> <br>
  <b> Figure-2: Entering Input </b>
</p>

***
There are two buttons “Quit” and “Enter to Code” at the bottom of the GUI.

Enter to Code: After entering all input, press the button “Enter to Code”. This button will take input from GUI and enter data to code.

Quit: After entering the data to code, press the button “Quit”. This button closes the GUI and launch Arena GUI as shown in Figure-3.


Arena GUI:

Arena GUI subscribe the Rostopic “Estimated_marker” and extract data from the topic

Note: Please Don’t change the topic name. For this GUI, “viewpoint_estimation” package topic name should be “Estimated_marker”.

<p align="center">
  <img src="https://github.com/simubhangu/Python_GUI/blob/master/Readme_images/c.png"> <br>
  <b> Figure-3: Arena GUI </b>
</p>

When the camera detect the Marker correctly then corresponding image will pop up on the provided coordinates. After detecting all markers according to input provided in Figure-2, GUI will look like as shown in Figure-4:


<p align="center">
  <img src="https://github.com/simubhangu/Python_GUI/blob/master/Readme_images/d.png"> <br>
  <b> Figure-3: Final GUI after detecting all markers </b>
</p>


Note: The above input is for illustration purpose only.




