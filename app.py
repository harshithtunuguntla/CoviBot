from flask import Flask, render_template, request, redirect, Response
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)




left_motor = 24
left_motor_back = 23

right_motor = 17
right_motor_back = 27

motor_speed = 25

uv_led1 = 20
uv_led2 = 21

front_led1 = 13
front_led2 = 19

ir_sensor = 6
sanitizer=7

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
GPIO.setup(sanitizer,GPIO.IN)



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