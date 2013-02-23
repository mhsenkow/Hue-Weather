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
                if code == "26":#tornado
                    l.bri(250)
                    l.alert()
                    for y in range(10):
                        for dim in range(10):
                            l.set_state({"bri": 250-dim*20,"xy": [0.1, y*0.1]})
                            time.sleep(0.01)
                        l.alert()
 
 
                elif code == "1":#tropical storm
                    l.bri(250)
                    l.alert()
                    for y in range(10):
                        for dim in range(10):
                            l.set_state({"bri": 250-dim*20,"xy": [0.3, y*0.1]})
                            time.sleep(0.01)
                        l.alert()		
 
 
                elif code == "2":#hurricane
                    l.bri(250)
                    l.alert()
                    for y in range(10):
                        for dim in range(10):
                            l.set_state({"bri": 250-dim*20,"xy": [0.5, y*0.1]})
                            time.sleep(0.01)
                        l.alert()		
 
                elif code == "3":#hurricane
                        l.bri(250)
                        l.alert()
                        for y in range(10):
                            for dim in range(10):
                                l.set_state({"bri": 250-dim*20,"xy": [0.5, y*0.1]})
                                time.sleep(0.01)
                            l.alert()
            if display == "temperature":
                l.bri(250)
                l.ct(154+int(thermo)*3)





 
    else:
        print 'No such city, try adding state'
get_condition(l1)
get_condition(l2)
get_condition(l3)