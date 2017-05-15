
from pubnub import Pubnub
import json,time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print "Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script"


#Setup GPIO
GPIO.setmode(GPIO.BOARD)

#Setup PubNub
pubnub = Pubnub(publish_key="pub-c-bd0276ed-f876-49cc-b73d-aa05b31efe63",subscribe_key="sub-c-76d94746-b211-11e4-b35d-02ee2ddab7fe")
pubnubChannelName = 'gpio-raspberry-control'


#Setup Glow Status Flow
glow = False


#PubNub Channel Subscribe Callback
def gpioCallback(msg,channel):

	global glow

	respstring = ''
	command = msg

	print "Command is : " + str(command)

	if('req' in command):
		if(command['req'] == 'toggle'):

			if(glow):
				glow = False;
				respstring = 'off'
			else:
				glow = True
				respstring = 'on'

			GPIO.output(16, glow)

			respmsg = {"resp" : respstring }
			pubnub.publish(pubnubChannelName, respmsg)


#PubNub Channel Subscribe Callback
def gpioError(msg):
	print 'Error :' + msg




if __name__ == '__main__':

	GPIO.setup(16, GPIO.OUT)

	pubnub.subscribe(pubnubChannelName, gpioCallback, gpioError)

	while True:

		time.sleep(5000)

		if(GPIO.gpio_function(16)):
			#All is over
			break

