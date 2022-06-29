# Car Detection

About: Car Detection is a python program that takes a video input, in this case 'highway.mp4', and creates a mask over the orignal video to identify and subsequently count cars shown in the MP4. The mask is created in a specific area of the video to keep the count of cars as accurate as possible. 

Functionality: Count the number of cars in a specified Area of interest on the MP4.

How to use:

1. Clone CarDetection from github using the `git clone https://github.com/EdArdolino/CarDetection.git`.
2. Open a Windows Powershell or Windows Command Prompt in the cloned location of CarDetect.py
3. Enter `python CarDetect.py` in the command line
4. Example: `'C:\Users\Admin\Documents\Python\OpenCV\CarDetection' python CarDetect.py`
5. The highway MP4 will pop up along with as layer mask and the area of interest where the program is focused on counting.
6. From here you will be able to see the program running and counting all of the vehicles as they approach the area of interest. 
7. In te console you will also see sets of coordinates, these are the coordinated of the vehicles on the screen
8. To exit the program, press `ESC` on your keybaord

Note:

Makes sure to clone the repo and leave as is, if not 'highway.mp4' may not function correctly.

If an issue arises with 'highway.mp4' not opening when the program is run, copy the direct path of 'highway.mp4' and paste into the quotes on line 8 in CarDetect.py
