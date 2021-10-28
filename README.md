# Number-Plate-Recognition-raspberrypi0w-
recognise number plates with one of the smallest single board computers
# How to setup
1. install raspberry pi os
2. set up the raspberrypi for headless install follow this <a href="https://core-electronics.com.au/tutorials/raspberry-pi-zerow-headless-wifi-setup.html">guide</a> (this will be the network you use to access the webGUI)
3. Run the following in your ssh session to open the raspberry pi cammera to the usb <a href="https://stackoverflow.com/questions/27950013/i-am-trying-make-the-raspberry-pi-camera-work-with-opencv">interface</a>
  sudo modprobe bcm2835-v4l2
  view it by typing this command : ls -ltrh /dev/video*
4. Pull my code to the Pi and install requirements.txt
5. set the python code to run at startup
6. done
# Issues and Questions
open an issue or question in the issue tab
