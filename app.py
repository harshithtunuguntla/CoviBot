from flask import Flask, render_template, request, redirect, Response
import time
import RPi.GPIO as GPIO
from flask.templating import render_template_string
GPIO.setwarnings(False)

import cv2
import face_recognition


cap = cv2.VideoCapture(-1)

motor_speed = 40
global lock


lock=False


left_motor = 24
left_motor_back = 23

right_motor = 17
right_motor_back = 27

uv_led1 = 20
uv_led2 = 21

front_led1 = 13
front_led2 = 19

ir_sensor = 6
sanitizer=7

GPIO_TRIGGER = 8
GPIO_ECHO = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor, GPIO.OUT)
GPIO.setup(right_motor, GPIO.OUT)
GPIO.setup(left_motor_back, GPIO.OUT)
GPIO.setup(right_motor_back, GPIO.OUT)

GPIO.setup(uv_led1, GPIO.OUT)
GPIO.setup(uv_led2, GPIO.OUT)

GPIO.setup(front_led1, GPIO.OUT)
GPIO.setup(front_led2, GPIO.OUT)

GPIO.setup(ir_sensor,GPIO.IN)
GPIO.setup(sanitizer,GPIO.OUT)

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

rm_pwm=GPIO.PWM(right_motor,1000)
rm_pwm.start(0)

rmb_pwm=GPIO.PWM(right_motor_back,1000)
rmb_pwm.start(0)

lm_pwm=GPIO.PWM(left_motor,1000)
lm_pwm.start(0)

lmb_pwm=GPIO.PWM(left_motor_back,1000)
lmb_pwm.start(0)


app = Flask(__name__)

#10000 - forward
#01000 - left
#00100 - stop
#00010 - right
#00001 - backward


if(GPIO.input(ir_sensor) == True):
    GPIO.output(sanitizer,GPIO.HIGH)


def move_bot_forward():
    if True:
        global motor_speed
        lm_pwm.ChangeDutyCycle(motor_speed)
        rm_pwm.ChangeDutyCycle(motor_speed)

        lmb_pwm.ChangeDutyCycle(0)
        rmb_pwm.ChangeDutyCycle(0)



        # GPIO.output(left_motor, GPIO.HIGH)
        # GPIO.output(right_motor, GPIO.HIGH)
        # GPIO.output(left_motor_back, GPIO.LOW)
        # GPIO.output(right_motor_back, GPIO.LOW)
        print("Sent Command to raspi - move f")
    else:
        print("in passs")
        pass

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
    pass

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

    pass

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
    pass

def move_bot_backward():
    global motor_speed
    lmb_pwm.ChangeDutyCycle(motor_speed)
    rmb_pwm.ChangeDutyCycle(motor_speed)

    lm_pwm.ChangeDutyCycle(0)
    rm_pwm.ChangeDutyCycle(0)
    # GPIO.output(left_motor_back, GPIO.HIGH)
    # GPIO.output(right_motor_back, GPIO.HIGH)
    # GPIO.output(left_motor, GPIO.LOW)
    # GPIO.output(right_motor, GPIO.LOW)
    print("Sent Command to raspi - move b")
    pass

def lights_on():
    GPIO.output(front_led1, GPIO.HIGH)
    GPIO.output(front_led2, GPIO.HIGH)
    print("Inside Lights on")
    pass

def lights_off():
    GPIO.output(front_led1, GPIO.LOW)
    GPIO.output(front_led2, GPIO.LOW)
    print("Inside Lights off")
    pass

def uv_on():
    print("Inside UV on")
    GPIO.output(uv_led1, GPIO.HIGH)
    GPIO.output(uv_led2, GPIO.HIGH)
    pass

def uv_off():
    print("Inside UV off")
    GPIO.output(uv_led1, GPIO.LOW)
    GPIO.output(uv_led2, GPIO.LOW)
    pass

def start_lockdown_procedure():

    global lock

    while lock:

        success,img = cap.read()
        # img = cv2.rotate(img, cv2.ROTATE_180)
        faceLoc1 = face_recognition.face_locations(img)
        print("faces" + str(faceLoc1))

        print(faceLoc1)

        if(faceLoc1):
        
            GPIO.output(buzzer,GPIO.HIGH)
            faceLoc = faceLoc1[0]
            print(faceLoc)
            cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
        else :
            GPIO.output(buzzer,GPIO.LOW)

        cv2.imshow("Image",img)
        cv2.waitKey(1)

def distance():
    print('Inside Distance')
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        print('Inside echo')
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        print('Inside trig')
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    print('exiting distance')
    return distance

@app.route('/')
def landing_page():
    return render_template("landing_page.html")


@app.route('/dashboard_1')
def dashboard_1():
    return render_template("dashboard_1.html")


@app.route('/dashboard_1/<val>')
def dashboard_1_action(val):
    if(val=="10000"):
        print("Bot Move Forward Command Activated")
        move_bot_forward()
    elif(val=="01000"):
        print("Bot Move Forward Command Activated")
        move_bot_left()
    elif(val=="00100"):
        print("Bot Move Forward Command Activated")
        move_bot_stop()
    elif(val=="00010"):
        print("Bot Move Forward Command Activated")
        move_bot_right()
    elif(val=="00001"):
        print("Bot Move Forward Command Activated")
        move_bot_backward()
    return '',204

@app.route('/lockdown')
def lockdown():
    return render_template('lockdown.html')

@app.route('/lockdown/start')
def lockdown_start():
    global lock
    lock=True
    start_lockdown_procedure()
    return '',204

@app.route('/lockdown/stop')
def lockdown_stop():
    global lock
    lock=False
    start_lockdown_procedure()

    print("Insidde Lockdown Stop")
    return '',204

@app.route('/monitoring')
def monitorning():
    return render_template('monitoring.html')

@app.route('/monitoring/start')
def monitoring_start():
    print("Insidde Monitoring Start")


    print(distance())
    if(distance()>10):
        move_bot_forward()
    else:
        move_bot_stop()
            
    return '',204

@app.route('/monitoring/stop')
def monitorning_stop():
    print('Inside Monitoring stop')
    move_bot_stop()
    return '',204

@app.route('/additional_settings',  methods=['POST','GET'])
def additional_settings():
    if request.method=='POST':
        print("inside post")
        value_received = request.form["entered_motor_value"]
        print(value_received)
        global motor_speed
        motor_speed = int(value_received)
        print(motor_speed)
        return '',204


    else:
        return render_template('additional_settings.html')

@app.route('/additional_settings/<val>')
def additional_settings_action(val):
    if(val=='l1'):
        print("Lights Turn on activated")
        lights_on()
    elif(val=="l0"):
        print("Lights Turn off activated")
        lights_off()
    elif(val=="u0"):
        print("UV Trun off activated")
        uv_off()
    elif(val=="u1"):
        print("UV Trun on activated")
        uv_on()
    return '',204
    





if __name__ == '__main__':
    app.run(debug=True)