from hue import Hue;
import time
h = Hue(); # Initialize the class
h.station_ip = "192.168.1.137"  # Your base station IP
h.get_state(); # Authenticate, bootstrap your lighting system
l = h.lights.get('l3')

switch = 1
description = "37" 
display = "weather" #or temperature


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

	while description == "5":#mixedrain and snow
		l.bri(250)
		l.set_state({"xy": [0.32,0.32]})
		l.bri(100)
		l.set_state({"xy": [0.2,0.1]})
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.32,0.32]})

	while description == "6":#mixedrain and sleet
		l.bri(250)
		l.set_state({"xy": [0.2,0.32]})
		l.bri(100)
		l.set_state({"xy": [0.2,0.1]})
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.32]})
		
	while description == "7":#mixed snow and sleet
		l.bri(250)
		l.set_state({"xy": [0.32,0.32]})
		l.bri(100)
		l.set_state({"xy": [0.32,0.32]})
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.32,0.32]})
		
	while description == "8":#freezing drizzle
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.1]})
		l.bri(100)
		time.sleep(0.01)
		l.set_state({"xy": [0.32,0.32]})
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.1]})

	while description == "9":#drizzle
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.1]})
		l.bri(100)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.1]})
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.1]})

	while description == "10":#freezing rain
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.1]})
		l.bri(100)
		time.sleep(0.01)
		l.set_state({"xy": [0.32,0.32]})
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.1]})
		
	while description == "11":#showers
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.13]})
		time.sleep(0.2)
		l.set_state({"xy": [0.2,0.1]})
		time.sleep(0.2)

	while description == "12":#showers
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.13]})
		time.sleep(0.2)
		l.set_state({"xy": [0.2,0.1]})
		time.sleep(0.2)

	while description == "13":#snow flurries
		l.bri(250)
		time.sleep(1)
		l.set_state({"xy": [0.2,0.2]})
		time.sleep(1)
		l.set_state({"bri": 150,"xy": [0.2,0.2]})
		time.sleep(0.4)
		l.bri(250)
		time.sleep(0.2)
		l.set_state({"xy": [0.2,0.2]})
		time.sleep(2)
		l.set_state({"bri": 180,"xy": [0.2,0.2]})
		time.sleep(0.3)
		
	while description == "14":#light snow showers
		l.bri(250)
		time.sleep(1)
		l.set_state({"xy": [0.2,0.2]})
		time.sleep(1)
		l.set_state({"bri": 150,"xy": [0.2,0.2]})
		time.sleep(0.4)
		l.bri(250)
		time.sleep(0.2)
		l.set_state({"xy": [0.2,0.2]})
		time.sleep(2)
		l.set_state({"bri": 180,"xy": [0.2,0.2]})
		time.sleep(0.3)
		
	while description == "15":#blowing snow
		l.bri(250)
		time.sleep(1)
		l.set_state({"xy": [0.2,0.2]})
		time.sleep(1)
		l.set_state({"bri": 150,"xy": [0.2,0.2]})
		time.sleep(0.4)
		l.bri(250)
		time.sleep(0.2)
		l.set_state({"xy": [0.2,0.2]})
		time.sleep(2)
		l.set_state({"bri": 180,"xy": [0.2,0.2]})
		time.sleep(0.3)
		
	while description == "16":#snow
		l.bri(250)
		l.set_state({"xy": [0.2,0.2]})
	
	while description == "17":#hail
		l.bri(250)
		l.set_state({"xy": [0.2,0.15]})
		l.alert()
		
	while description == "18":#sleet
		l.bri(250)
		l.set_state({"xy": [0.32,0.32]})
		l.bri(100)
		l.set_state({"xy": [0.32,0.32]})
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.32,0.32]})

	while description == "19":#dust
		l.set_state({"bri": 120,"xy": [0.1,0.5]})
		
	while description == "20":#foggy
		l.set_state({"bri": 70,"xy": [0.1,0.2]})

	while description == "21":#haze
		l.set_state({"bri": 70,"xy": [0.1,0.5]})
		
	while description == "22":#smoky
		l.set_state({"bri": 120,"xy": [0.1,0.5]})

	while description == "23":#blustery
		l.set_state({"bri": 70,"xy": [0.1,0.2]})

	while description == "24":#windy
		l.set_state({"bri": 70,"xy": [0.1,0.5]})
		
	while description == "25":#cold
		l.set_state({"bri": 250,"xy": [0.2,0.2]})

	while description == "26":#cloudy
		l.set_state({"bri": 120,"xy": [0.2,0.2]})

	while description == "27":#mostly cloud night
		l.set_state({"bri": 10,"xy": [0.2,0.2]})

	while description == "28":#mostly cloudy day
		l.set_state({"bri": 120,"xy": [0.45,0.5]})

	while description == "29":#partly cloudy night
		l.set_state({"bri": 70,"xy": [0.2,0.2]})

	while description == "30":#partly cloudy day
		l.set_state({"bri": 160,"xy": [0.45,0.5]})

	while description == "31":#clear night
		l.set_state({"bri": 50,"xy": [0.2,0.2]})  
		
	while description == "32":#sunny
		l.bri(250)
		for ct in range(100):
			l.ct(500-ct*2)
		for ct in range(100):
			l.ct(400+ct*2)	
		
	while description == "33":#fair(night)
		l.bri(50)
		for ct in range(100):
			l.ct(500-ct*2)
		for ct in range(100):
			l.ct(400+ct*2)
			
	while description == "34":#fair(day)
		l.bri(200)
		for ct in range(100):
			l.ct(500-ct*2)
		for ct in range(100):
			l.ct(400+ct*2)
		
	while description == "35":#mixedrain and hail
		l.bri(250)
		l.set_state({"xy": [0.2,0.32]})
		l.bri(100)
		l.set_state({"xy": [0.2,0.1]})
		l.bri(250)
		time.sleep(0.01)
		l.set_state({"xy": [0.2,0.32]})

	while description == "36":#hot
		l.bri(250)
		l.set_state({"xy": [0.7,0.3]})
		for dim in range(15):
			l.bri(250-dim*10)
		for dim in range(15):
			l.bri(100+dim*10)
			
	while description == "37":#isolated thunderstorms
		l.bri(250)
		l.alert()
		for y in range(5):
			for dim in range(10):
				l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
		l.alert()		
		switch = switch*-1
		l.ct(600)
		l.alert("lselect")
		
	while description == "38":#scattered thunderstorms
		l.bri(250)
		l.alert()
		for y in range(5):
			for dim in range(10):
				l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
		l.alert()		
		switch = switch*-1
		l.ct(600)
		l.alert("lselect")
		
	while description == "39":#scattered thunderstorms
		l.bri(250)
		l.alert()
		for y in range(5):
			for dim in range(10):
				l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
		l.alert()		
		switch = switch*-1
		l.ct(600)
		l.alert("lselect")

	while description == "40":#scattered showers
		l.bri(250)
		l.alert()
		for y in range(5):
			for dim in range(10):
				l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
		l.alert()		
		switch = switch*-1
		
	while description == "41":#heavy snow
		l.bri(250)
		l.set_state({"xy": [0.2,0.2]})
		
	while description == "42":#scattered snow showers
		l.set_state({"bri": 120,"xy": [0.2,0.2]})
		
	while description == "43":#heavy snow
		l.bri(250)
		l.set_state({"xy": [0.2,0.2]})

	while description == "44":#partly cloudy
		l.set_state({"bri": 120,"xy": [0.2,0.2]})
		
	while description == "45":#thundershowers
		l.bri(250)
		l.alert()
		for y in range(5):
			for dim in range(10):
				l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
		l.alert()		
		switch = switch*-1
		l.ct(600)
		l.alert("lselect")
		
	while description == "46":#snow showers
		l.bri(250)
		l.alert()
		for y in range(5):
			for dim in range(10):
				l.set_state({"bri": 250-dim*30,"xy": [0.2, y*0.1]})
		l.alert()		
		switch = switch*-1
		l.ct(600)
		l.alert("lselect")
			
	while description == "47":#isolated thundershowers
		l.bri(250)
		l.alert()
		for y in range(5):
			for dim in range(10):
				l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
		l.alert()		
		switch = switch*-1
		l.ct(600)
		l.alert("lselect")
	
		
		
		
#TEMPERATURE
if display == "temperature":#hot
	l.bri(250)
	l.ct(154+temp*3)

#l.toggle()
#l.alert() # short alert
#l.alert("lselect") # long alert
