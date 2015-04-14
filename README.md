# PubNub-RaspberryPi-RemoteControl
PubNub IoT Technical Use Case - Controlling a Raspberry Pi device remotely through browser

## INTRODUCTION
A simple IoT application to demonstrate how an LED device attached to a Raspberry Pi B+ board can be switched on or off remotely from a web browser by sending control messages over PubNub data stream network.


## PREREQUISITES
1. Setup the hardware as per the schematic drawing provided in Schematic.jpg file
2. Power on the Raspberry Pi, and make sure that it is running Raspbian OS with python 2 installed. 
3. Ensure that internet connectivity is available and RPi GPIO Python library is installed.
 

## USAGE
1. Run the python driver code 'driver/pidriver.py' from the python interpreter on the Raspberry Pi console.
2. Launch a web browser in another computer and open the 'controller/index.html' page file in it.
3. Press the TOGGLE button on the web page to toggle the glowing state of the LED connected to the Raspberry Pi. The current state on the LED device is also reflected on the web page. Click on the button several times to see the LED state alternating between on and off. 

## PITFALLS
1. The pidriver.py script may not shut down gracefully on pressing Ctrl-C on keyboard. The workaround is to kill the python process using unix kill command on Raspberry Pi console.
