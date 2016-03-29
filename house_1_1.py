import serial, urllib,os,datetime
from ouimeaux.environment import Environment
from time import gmtime,strftime
import httplib, urllib
import pyowm
import time

fh=open("log.txt","a")

temp_boost=0.1
env=Environment()
env.start()
boiler=env.get_switch('Boiler')

boiler_state=[]

port = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout = 120)

boiler_off_temp=0
boiler_on_temp=99
porch=[]
landing=[]
garden=[]
battery='x.xx'
print 'starting'
while True:
        error = ''
#    try:    
        try:        
            rcv = port.read(12)
        except:
            error = error + ' Port read failure'

        print ("Message: " + repr(rcv))  
        t=datetime.datetime.now().time()
        hour=int(t.hour)
        minute=int(t.minute)

        try:
            owm=pyowm.OWM('23e3029b9032fba1e89c853013ff52f7')
            observation=owm.weather_at_place('hereford uk')
            w=observation.get_weather()
            a=(w.get_temperature('celsius'))
            outside_temp = a['temp']
            print 'Outside temperature ',outside_temp
        except:
            error = error + ' Outside temperature read failure'

	#default temperatures in case time settings fails
        boiler_off_temp = 20.0
        boiler_on_temp = 19.8

        if hour == 1:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 1'
            garden = 'off'

        if hour == 2:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 1'
            garden = 'off'

        if hour == 3:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 1'
            garden = 'off'

        if hour == 4:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 1'
            garden = 'off'

        if hour == 5:
            boiler_off_temp = 18.0
            boiler_on_temp = 17.8
	    porch = 'off'
            landing = 'on 50'
            garden = 'off'

        if hour == 6:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'on 50'
            landing = 'on 50'
            garden = 'on 50'

        if hour == 7:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'on 50'
            landing = 'on 250'
            garden = 'on 50'

        if hour == 8:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'on 50'
            landing = 'on 250'
            garden = 'on 50'

        if hour == 9:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'off'
            landing = 'on 50'
            garden = 'off'

        if hour == 10:
            boiler_off_temp = 18.0
            boiler_on_temp = 17.8
	    porch = 'off'
            landing = 'off'
            garden = 'off'

        if hour == 11:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 10'
            garden = 'off'

        if hour == 12:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 10'
            garden = 'off'

        if hour == 13:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 10'
            garden = 'off'

        if hour == 14:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 10'
            garden = 'off'

        if hour == 14:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 10'
            garden = 'off'

        if hour == 15:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 10'
            garden = 'off'

        if hour == 16:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'on 50'
            landing = 'on 50'
            garden = 'on 50'

        if hour == 17:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'on 50'
            landing = 'on 50'
            garden = 'on 50'

        if hour == 18:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'on 150'
            landing = 'on 150'
            garden = 'on 250'

        if hour == 19:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'on 150'
            landing = 'on 250'
            garden = 'on 250'

        if hour == 20:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'on 150'
            landing = 'on 250'
            garden = 'on 250'

        if hour == 21:
            boiler_off_temp = 20.0
            boiler_on_temp = 19.8
	    porch = 'on 150'
            landing = 'on 250'
            garden = 'on 250'

        if hour == 22:
            boiler_off_temp = 19.0
            boiler_on_temp = 18.8
	    porch = 'on 50'
            landing = 'on 100'
            garden = 'on 50'

        if hour == 23:
            boiler_off_temp = 18.0
            boiler_on_temp = 17.8
	    porch = 'on 50'
            landing = 'on 50'
            garden = 'on 50'

        if hour == 0:
            boiler_off_temp = 17.0
            boiler_on_temp = 16.8
	    porch = 'off'
            landing = 'on 1'
            garden = 'off'

	#boost thermostat settings
        boiler_off_temp = boiler_off_temp + temp_boost
        boiler_on_temp = boiler_on_temp + temp_boost

	# remember landing at porch bulbs swapped
        #os.system('wemo light garden ' + str(garden))
        os.system('wemo light porch ' + str(landing))
        #os.system('wemo light porch ' + str(landing))

        msg = rcv[3:7] 
        if msg == 'BATT':
            battery=rcv[7:11]
        
        if msg == 'TEMP':
            temp = float(rcv[8:12])
            if temp > boiler_off_temp:
                boiler.off()
            elif temp < boiler_on_temp:
                boiler.on()    
        
            if (boiler.get_state()):
                boiler_state = "BoilerOn"
            else:
                boiler_state="BoilerOff"
            house_status = strftime("%Y-%m-%d %H:%M",gmtime())+' '+str(outside_temp)+' '+str(temp)+' '+str(boiler_on_temp)+' '+str(boiler_off_temp)+' '+boiler_state + ' P='+str(porch)+' L='+str(landing)+' G='+str(garden) + ' B='+str(battery) + str(error)
            print house_status
            try:
                fh.write('\n'+house_status)
                fh.flush()
            except:
                error = error + ' Failed Logfile write'

            try:
                urllib.urlretrieve("http://andythegrouch.pythonanywhere.com/msg/"+house_status, filename= "test.txt")
            except:
                error = error + ' Failed to upload status to cloud'
            
        if error != '' :
            print 'Error:' + str(error)

                
#    except:
#        house_alarm = strftime("%Y-%m-%d %H:%M",gmtime())+' House control fail'
#        conn = httplib.HTTPSConnection("api.pushover.net:443")
#        conn.request("POST", "/1/messages.json", urllib.urlencode({"token": "azKQQ8HQ4Mtnp3ZdRr84NDwPSCiFXL","user": "uSncjb7Z3vANw1rEooowkqDgrGQtZq","message": house_alarm,}), { "Content-type": "application/x-www-form-urlencoded" })
#        conn.getresponse()
#        fh.write('\n'+house_alarm)
#        fh.flush()
        


