#item 1 
from gpiozero import Servo
from time import sleep

GPIO.setmode(GPIO.BCM)
print("Starting Servo")


servo = 25#Servo(25)
GPIO.setup(servo, GPIO.OUT)

#real code?
pwm = GPIO.PWM(servo, 1000)#1000 is the pin freqiuency

try:
    pwm.start(50)
    sleep(1.0)
    pwm.stop()
    sleep(1.0)

except KeyboardInterrupt:
	print("Program stopped")

"""
try:
    while True:
        servo.min()
        sleep(0.5)
        servo.mid()
        sleep(0.5)
        servo.max()
        sleep(0.5)
except KeyboardInterrupt:
	print("Program stopped")
	
#item 2
"""
"""
from gpiozero import Servo
from time import sleep

servo = Servo(25)
val = -1

try:
    while True:
        servo.value = val
        sleep(0.1)
        val = val + 0.1
        if val > 1:
        	val = -1
except KeyboardInterrupt:
	print("Program stopped")
"""