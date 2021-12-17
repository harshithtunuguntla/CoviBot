import RPi.GPIO as GPIO

from time import sleep

led_pin=27
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
pwm=GPIO.PWM(led_pin,100)
pwm.start(0)

pwm.ChangeDutyCycle(50)



# for x in range(100):
#     pwm.ChangeDutyCycle(x)
#     sleep(0.1)

# for x in range(100,-1,-1):
#     pwm.ChangeDutyCycle(x)
#     sleep(0.1)

GPIO.cleanup()

