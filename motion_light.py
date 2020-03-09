
   # Motion detection using PIR on raspberry Pi


import RPi.GPIO as GPIO

PIR_input = 19#read PIR Output
#PIR_input = 21

#FAN = 16
LED = 13                #LED for signalling motion detected 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)        #choose pin no. system
GPIO.setup(PIR_input, GPIO.IN)  
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)
#GPIO.setup(FAN, GPIO.OUT)
#GPIO.output(FAN, GPIO.LOW)

while True:
#when motion detected turn on LED
    if(GPIO.input(PIR_input)):
        GPIO.output(LED, GPIO.HIGH)
        #GPIO.output(FAN, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
        #GPIO.output(FAN, GPIO.LOW)