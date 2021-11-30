import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)

# pwm = GPIO.PWM(18, 1000)
# pwm.start(50)
# pwm.ChangeDutyCycle(75)

# if GPIO.input(17):
#     print("Pin 11 is HIGH")
# else:
#     print("Pin 11 is LOW")

# time.sleep(0.25)