#Wheels Testing Module
import RPi.GPIO as GPIO
GPIO.setwarnings(False)


left_motor = 17
left_motor_back = 27


right_motor = 23
right_motor_back = 24


GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor, GPIO.OUT)
GPIO.setup(right_motor, GPIO.OUT)
GPIO.setup(left_motor_back, GPIO.OUT)
GPIO.setup(right_motor_back, GPIO.OUT)


while True:
    nl = [17,27,23,24]

    inp = int(input("Enter testing pin : "))
    inp2 = int(input("Enter testing pin 2 : "))

    nl.remove(inp)
    if(inp2!=0):
        nl.remove(inp2)

        
    GPIO.output(inp,GPIO.LOW)
    
    if(inp2!=0):
        GPIO.output(inp2,GPIO.HIGH)



    for pin in nl:
        GPIO.output(pin,GPIO.LOW)

    print('-------------------\n')



    



# a = int(input(("Enter active pin number ")))
# GPIO.output(a, GPIO.HIGH)

# b = int(input(("Enter deactive pin number 1 ")))
# c = int(input(("Enter deactive pin number 2 ")))
# d = int(input(("Enter deactive pin number 3 ")))
# GPIO.output(b, GPIO.LOW)
# GPIO.output(c, GPIO.LOW)
# GPIO.output(d, GPIO.LOW)
