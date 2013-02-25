import mechanize
import urllib, urllib2, re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import json
import threading
import random
from hue import Hue;
import time
 
h = Hue(); # Initialize the class
h.station_ip = "192.168.1.137"  # Your base station IP
h.get_state(); # Authenticate, bootstrap your lighting system
l1 = h.lights.get('l1')
l2 = h.lights.get('l2')
l3 = h.lights.get('l3')		
 
def get_condition(l):
 
	location = raw_input('Insert a city: ') 
	lightChoice = raw_input('Which light do you want?(1,2 or 3)') 
	display = raw_input('Do you want to see the weather or temperature?')
	location = location.replace(',', '')
 
	# Browser
	br = mechanize.Browser()

	# Open some site, let's pick a random one, the first that pops in mind:
	r = br.open('http://isithackday.com/geoplanet-explorer/')
	html = r.read()

	# get to form and populate with location
	br.select_form(nr=0)
	br.form['start'] = location

	# submit and read the response url
	response = br.submit()
	response = response.geturl()

	# extract woeid 
	woeid = response[-7:]
 
	if woeid.isdigit():

		print('WOEID: ' + str(woeid))
		# Send the WOEID to Yahoo Weather
		weather = ''
		url = 'http://weather.yahooapis.com/forecastrss?w=' + str(woeid)
		response = urllib2.urlopen(url)
		data = response.read()

		# Load XML results as string
		root = ET.fromstring(data)        

		# Find location in results
		city = root.find('.//description').text
		city = re.sub('Yahoo! Weather for ', '', city)
		print('City Name: ' + str(city))

		WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

		for element in root.findall('channel/item/{%s}condition' % WEATHER_NS):
			condition = element.get('text')
			thermo = element.get('temp')
			code = element.get('code')
			print('Current Condition: ' + condition)
			print('Condition Code: ' + code)
			print('Temperature: ' + thermo)

			if display == "weather":
				if code == "0":#tornado
					l.bri(250)
					l.alert()
					for y in range(10):
						for dim in range(10):
							l.set_state({"bri": 250-dim*20,"xy": [0.1, y*0.1]})
							time.sleep(0.01)
					l.alert()		
					switch = switch*-1


				elif code == "1":#tropical storm
					l.bri(250)
					l.alert()
					for y in range(10):
						for dim in range(10):
							l.set_state({"bri": 250-dim*20,"xy": [0.3, y*0.1]})
							time.sleep(0.01)
					l.alert()		
					switch = switch*-1


				elif code == "2":#hurricane
					l.bri(250)
					l.alert()
					for y in range(10):
						for dim in range(10):
							l.set_state({"bri": 250-dim*20,"xy": [0.5, y*0.1]})
							time.sleep(0.01)
					l.alert()		
					switch = switch*-1


				elif code == "3":#severe thunderstorms
					l.bri(250)
					l.alert()
					for y in range(5):
						for dim in range(10):
							l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
					l.alert()		
					switch = switch*-1
					l.ct(600)
					l.alert("lselect")
					
				elif code == "4":#thunderstorms
					l.bri(250)
					l.alert()
					for y in range(5):
						for dim in range(10):
							l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
					l.alert()		
					switch = switch*-1
					l.bri(250)
					l.ct(600)
					
				elif code == "5":#mixedrain and snow
					l.bri(250)
					l.set_state({"xy": [0.32,0.32]})
					l.bri(100)
					l.set_state({"xy": [0.2,0.1]})
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.32,0.32]})

				elif code == "6":#mixedrain and sleet
					l.bri(250)
					l.set_state({"xy": [0.2,0.32]})
					l.bri(100)
					l.set_state({"xy": [0.2,0.1]})
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.32]})

				elif code == "7":#mixed snow and sleet
					l.bri(250)
					l.set_state({"xy": [0.32,0.32]})
					l.bri(100)
					l.set_state({"xy": [0.32,0.32]})
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.32,0.32]})

				elif code == "8":#freezing drizzle
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.1]})
					l.bri(100)
					time.sleep(0.01)
					l.set_state({"xy": [0.32,0.32]})
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.1]})

				elif code == "9":#drizzle
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.1]})
					l.bri(100)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.1]})
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.1]})

				elif code == "10":#freezing rain
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.1]})
					l.bri(100)
					time.sleep(0.01)
					l.set_state({"xy": [0.32,0.32]})
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.1]})

				elif code == "11":#showers
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.13]})
					time.sleep(0.2)
					l.set_state({"xy": [0.2,0.1]})
					time.sleep(0.2)

				elif code == "12":#showers
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.13]})
					time.sleep(0.2)
					l.set_state({"xy": [0.2,0.1]})
					time.sleep(0.2)

				elif code == "13":#snow flurries
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

				elif code == "14":#light snow showers
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

				elif code == "15":#blowing snow
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

				elif code == "16":#snow
					l.bri(250)
					l.set_state({"xy": [0.2,0.2]})

				elif code == "17":#hail
					l.bri(250)
					l.set_state({"xy": [0.2,0.15]})
					l.alert()

				elif code == "18":#sleet
					l.bri(250)
					l.set_state({"xy": [0.32,0.32]})
					l.bri(100)
					l.set_state({"xy": [0.32,0.32]})
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.32,0.32]})

				elif code == "19":#dust
					l.set_state({"bri": 120,"xy": [0.1,0.5]})

				elif code == "20":#foggy
					l.set_state({"bri": 70,"xy": [0.1,0.2]})

				elif code == "21":#haze
					l.set_state({"bri": 70,"xy": [0.1,0.5]})

				elif code == "22":#smoky
					l.set_state({"bri": 120,"xy": [0.1,0.5]})

				elif code == "23":#blustery
					l.set_state({"bri": 70,"xy": [0.1,0.2]})

				elif code == "24":#windy
					l.set_state({"bri": 70,"xy": [0.1,0.5]})

				elif code == "25":#cold
					l.set_state({"bri": 250,"xy": [0.2,0.2]})

				elif code == "26":#cloudy
					l.set_state({"bri": 120,"xy": [0.2,0.2]})

				elif code == "27":#mostly cloud night
					l.set_state({"bri": 10,"xy": [0.2,0.2]})

				elif code == "28":#mostly cloudy day
					l.set_state({"bri": 120,"xy": [0.45,0.5]})

				elif code == "29":#partly cloudy night
					l.set_state({"bri": 70,"xy": [0.2,0.2]})

				elif code == "30":#partly cloudy day
					l.set_state({"bri": 160,"xy": [0.45,0.5]})

				elif code == "31":#clear night
					l.set_state({"bri": 50,"xy": [0.2,0.2]})  

				elif code == "32":#sunny
					l.bri(250)
					for ct in range(100):
						l.ct(500-ct*2)
					for ct in range(100):
						l.ct(400+ct*2)	

				elif code == "33":#fair(night)
					l.bri(50)
					for ct in range(100):
						l.ct(500-ct*2)
					for ct in range(100):
						l.ct(400+ct*2)

				elif code == "34":#fair(day)
					l.bri(200)
					for ct in range(100):
						l.ct(500-ct*2)
					for ct in range(100):
						l.ct(400+ct*2)

				elif code == "35":#mixedrain and hail
					l.bri(250)
					l.set_state({"xy": [0.2,0.32]})
					l.bri(100)
					l.set_state({"xy": [0.2,0.1]})
					l.bri(250)
					time.sleep(0.01)
					l.set_state({"xy": [0.2,0.32]})

				elif code == "36":#hot
					l.bri(250)
					l.set_state({"xy": [0.7,0.3]})
					for dim in range(15):
						l.bri(250-dim*10)
					for dim in range(15):
						l.bri(100+dim*10)

				elif code == "37":#isolated thunderstorms
					l.bri(250)
					l.alert()
					for y in range(5):
						for dim in range(10):
							l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
					l.alert()		
					switch = switch*-1
					l.ct(600)
					l.alert("lselect")

				elif code == "38":#scattered thunderstorms
					l.bri(250)
					l.alert()
					for y in range(5):
						for dim in range(10):
							l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
					l.alert()		
					switch = switch*-1
					l.ct(600)
					l.alert("lselect")

				elif code == "39":#scattered thunderstorms
					l.bri(250)
					l.alert()
					for y in range(5):
						for dim in range(10):
							l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
					l.alert()		
					switch = switch*-1
					l.ct(600)
					l.alert("lselect")

				elif code == "40":#scattered showers
					l.bri(250)
					l.alert()
					for y in range(5):
						for dim in range(10):
							l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
					l.alert()		
					switch = switch*-1

				elif code == "41":#heavy snow
					l.bri(250)
					l.set_state({"xy": [0.2,0.2]})

				elif code == "42":#scattered snow showers
					l.set_state({"bri": 120,"xy": [0.2,0.2]})

				elif code == "43":#heavy snow
					l.bri(250)
					l.set_state({"xy": [0.2,0.2]})

				elif code == "44":#partly cloudy
					l.set_state({"bri": 120,"xy": [0.2,0.2]})

				elif code == "45":#thundershowers
					l.bri(250)
					l.alert()
					for y in range(5):
						for dim in range(10):
							l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
					l.alert()		
					switch = switch*-1
					l.ct(600)
					l.alert("lselect")

				elif code == "46":#snow showers
					l.bri(250)
					l.alert()
					for y in range(5):
						for dim in range(10):
							l.set_state({"bri": 250-dim*30,"xy": [0.2, y*0.1]})
					l.alert()		
					switch = switch*-1
					l.ct(600)
					l.alert("lselect")

				elif code == "47":#isolated thundershowers
					l.bri(250)
					l.alert()
					for y in range(5):
						for dim in range(10):
							l.set_state({"bri": 250-dim*30,"xy": [0.1, y*0.1]})
					l.alert()		
					switch = switch*-1
					l.ct(600)
					l.alert("lselect")


			if display == "temperature":
			    l.bri(250)
			    l.ct(154+int(thermo)*3)



	else:
		print 'No such city, try adding state'
get_condition(l1)
get_condition(l2)
get_condition(l3)