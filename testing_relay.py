import RPi.GPIO as GPIO
sanitizer_pin = 12

ir_sensor_pin = 6
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(sanitizer_pin, GPIO.OUT)
GPIO.setup(ir_sensor_pin, GPIO.IN)

while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(ir_sensor_pin): # if port 25 == 1  
            print("Called")
            GPIO.output(sanitizer_pin, 0)         # set port/pin value to 1/HIGH/True  
        else:   
            GPIO.output(sanitizer_pin, 1)  