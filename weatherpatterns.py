from hue import Hue;
import time
h = Hue(); # Initialize the class
h.station_ip = "192.168.1.137"  # Your base station IP
h.get_state(); # Authenticate, bootstrap your lighting system
l = h.lights.get('l3')

switch = 1
description = "4" 
display = "temperature" #or temperature


temp = 75

if display == "weather":
	while description == "0":#tornado
		l.bri(250)
		l.alert()
		for y in range(10):
			for dim in range(10):
				l.set_state({"bri": 250-dim*20,"xy": [0.1, y*0.1]})
				time.sleep(0.01)
		l.alert()		
		switch = switch*-1


	while description == "1":#tropical storm
		l.bri(250)
		l.alert()
		for y in range(10):
			for dim in range(10):
				l.set_state({"bri": 250-dim*20,"xy": [0.3, y*0.1]})
				time.sleep(0.01)
		l.alert()		
		switch = switch*-1


	while description == "2":#hurricane
		l.bri(250)
		l.alert()
		for y in range(10):
			for dim in range(10):
				l.set_state({"bri": 250-dim*20,"xy": [0.5, y*0.1]})
				time.sleep(0.01)
		l.alert()		
		switch = switch*-1

	while description == "3":#severe thunderstorms
		l.bri(250)
		l.alert()
		for y in range(5):
			for dim in range(10):
				l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
		l.alert()		
		switch = switch*-1
		l.ct(600)
		l.alert("lselect")


	while description == "4":#thunderstorms
		l.bri(250)
		l.alert()
		for y in range(5):
			for dim in range(10):
				l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
		l.alert()		
		switch = switch*-1
		l.bri(250)
		l.ct(600)


	while description == "32":#sunny
		l.bri(250)
		for ct in range(100):
			l.ct(500-ct*2)
		for ct in range(100):
			l.ct(400+ct*2)	
		
	while description == "33":#fair(night)
		l.bri(250)
		for ct in range(100):
			l.ct(500-ct*2)
		for ct in range(100):
			l.ct(400+ct*2)

	while description == "36":#hot
		l.bri(250)
		l.set_state({"xy": [0.7,0.3]})
		for dim in range(15):
			l.bri(250-dim*10)
		for dim in range(15):
			l.bri(100+dim*10)
		
		
		
		
#TEMPERATURE
if display == "temperature":#hot
	l.bri(250)
	l.ct(154+temp*3)

#l.toggle()
#l.alert() # short alert
#l.alert("lselect") # long alert
