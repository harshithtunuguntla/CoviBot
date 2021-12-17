

import RPi.GPIO as GPIO
import time
 
GPIO.cleanup()

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 8
GPIO_ECHO = 25

left_motor = 24
left_motor_back = 23

right_motor = 17
right_motor_back = 27

# motor_speed=60

global motor_speed
motor_speed = 40


#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

GPIO.setup(left_motor, GPIO.OUT)
GPIO.setup(right_motor, GPIO.OUT)
GPIO.setup(left_motor_back, GPIO.OUT)
GPIO.setup(right_motor_back, GPIO.OUT)



rm_pwm=GPIO.PWM(right_motor,1000)
rm_pwm.start(0)

rmb_pwm=GPIO.PWM(right_motor_back,1000)
rmb_pwm.start(0)

lm_pwm=GPIO.PWM(left_motor,1000)
lm_pwm.start(0)

lmb_pwm=GPIO.PWM(left_motor_back,1000)
lmb_pwm.start(0)



def move_bot_forward():
    global motor_speed
    lm_pwm.ChangeDutyCycle(motor_speed)
    rm_pwm.ChangeDutyCycle(motor_speed)

    lmb_pwm.ChangeDutyCycle(0)
    rmb_pwm.ChangeDutyCycle(0)



def move_bot_left():
    global motor_speed
    lmb_pwm.ChangeDutyCycle(motor_speed)
    rm_pwm.ChangeDutyCycle(motor_speed)

    lm_pwm.ChangeDutyCycle(0)
    rmb_pwm.ChangeDutyCycle(0)
    # GPIO.output(left_motor, GPIO.LOW)
    # GPIO.output(right_motor, GPIO.HIGH)
    # GPIO.output(left_motor_back, GPIO.HIGH)
    # GPIO.output(right_motor_back, GPIO.LOW)
    print("Sent Command to raspi - move l")
    

def move_bot_stop():
    global motor_speed
    lmb_pwm.ChangeDutyCycle(0)
    rm_pwm.ChangeDutyCycle(0)

    lm_pwm.ChangeDutyCycle(0)
    rmb_pwm.ChangeDutyCycle(0)
    # GPIO.output(left_motor, GPIO.LOW)
    # GPIO.output(right_motor, GPIO.LOW)
    # GPIO.output(left_motor_back, GPIO.LOW)
    # GPIO.output(right_motor_back, GPIO.LOW)
    print("Sent Command to raspi - move s")


def move_bot_right():
    global motor_speed
    lm_pwm.ChangeDutyCycle(motor_speed)
    rmb_pwm.ChangeDutyCycle(motor_speed)

    lmb_pwm.ChangeDutyCycle(0)
    rm_pwm.ChangeDutyCycle(0)
    # GPIO.output(left_motor, GPIO.HIGH)
    # GPIO.output(right_motor, GPIO.LOW)
    # GPIO.output(left_motor_back, GPIO.LOW)
    # GPIO.output(right_motor_back, GPIO.HIGH)
    print("Sent Command to raspi - move r")


 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print(dist)
            if(dist>10):
                move_bot_forward()
            else:
                move_bot_stop()

            # print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()