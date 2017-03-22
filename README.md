# Python_GUI
This package Contain the Pyhton GUI for Explorer Bot Theme

Package Required:
Tkinter: sudo apt-get install python-tk	
Python Imaging Library(PIL): sudo apt-get install python-PIL

Follow the following instruction
1. Clone the git repository into Laptop/PC and visit to that directory.
2. Run the “final_gui.py” scripts and this script will launch one GUI as follow:

***
![img-1](https://github.com/simubhangu/Python_GUI/blob/master/Readme_images/a.png)
Figure-1: Gui for enter Input

In this GUI you can enter the detail according to provided input
1. Number of Markers: Total number of marker present in arena: Maximum will be 8 
2. Marker_Cordinates_*: Coordinates of marker in the arena eg: 1,1 or 2,2 ( Please Don’t add any brackets while entering data)
3. Marker_ID: Marker ID of the object place at respective coordinate. eg: 202, 210 etc.


After entering the input, Gui will be look like:
![img-2](https://github.com/simubhangu/Python_GUI/blob/master/Readme_images/b.png)

-> Figure 2: Entering Input <-

***
At the end of Gui two buttons are “Quit” and “Enter to Code”.
Enter to Code: After entering all input, press the button “Enter to Code”. This button will take input from GUI and enter data to code.
Quit: After entering the data to code, press the button “Quit”. This button quit this GUi and launch another GUI.Refer Figure 3.

Arena GUI:

After Quit the “Enter Inputs” GUI. “The Explorer Bot” GUI will pop up. This GUI subscribe the Rostopic “Estimated_marker” extract data from that topic
Note: Please Don’t change the topic name. For this GUI, “viewpoint_estimation” package topic name should be  “Estimated_marker”.


![img-3](https://github.com/simubhangu/Python_GUI/blob/master/Readme_images/c.png)
Figure 3: Arena GUI

When the camera Detect the Marker Correctly then corresponding image will be pop up on the provided Coordinates. After detecting the all marker according to input provided in figure-2 Gui will be look like as shown in Figure-4:
![img-4](https://github.com/simubhangu/Python_GUI/blob/master/Readme_images/d.png)
Figure: 4: Final GUI after detecting all marker

Note: The above input is only used just as an example for explaining GUI.




