import pyupm_adxl345 as adxl
import mraa
import time
device = adxl.Adxl345(0)

pin = mraa.Pwm(18)
pin.period_ms(2)
pin.enable(True)

while True:
	device.update()
	a = device.getAcceleration()
	
	
	if a[2]>0 :
		pin.write(0.2)
		print "(x,y,z)=%5.2f, %5.2f, %5.2f" % (a[0], a[1], a[2])
		print "speed=0.2"
	elif a[2] > -0.7 and a[2] <= 0 :
	    	pin.write(0.6)
		print "(x,y,z)=%5.2f, %5.2f, %5.2f" % (a[0], a[1], a[2])
		print "speed=0.6"
	else :
		pin.write(1)
		print "(x,y,z)=%5.2f, %5.2f, %5.2f" % (a[0], a[1], a[2])
		print "speed=1"
		
	time.sleep(0.3)

