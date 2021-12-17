from flask import Flask, render_template, request, redirect, Response
import time
# import RPi.GPIO as GPIO
# GPIO.setwarnings(False)




# left_motor = 23
# left_motor_back = 24

# right_motor = 17
# right_motor_back = 27

# motor_speed = 25


# GPIO.setmode(GPIO.BCM)
# GPIO.setup(left_motor, GPIO.OUT)
# GPIO.setup(right_motor, GPIO.OUT)
# GPIO.setup(left_motor_back, GPIO.OUT)
# GPIO.setup(right_motor_back, GPIO.OUT)


app = Flask(__name__)

#10000 - forward
#01000 - left
#00100 - stop
#00010 - right
#00001 - backward




def move_bot_forward():
    GPIO.output(left_motor, GPIO.HIGH)
    GPIO.output(right_motor, GPIO.HIGH)
    GPIO.output(left_motor_back, GPIO.LOW)
    GPIO.output(right_motor_back, GPIO.LOW)
    print("Sent Command to raspi - move f")
    pass

def move_bot_left():
    GPIO.output(left_motor, GPIO.LOW)
    GPIO.output(right_motor, GPIO.HIGH)
    GPIO.output(left_motor_back, GPIO.HIGH)
    GPIO.output(right_motor_back, GPIO.LOW)
    print("Sent Command to raspi - move l")
    pass

def move_bot_stop():
    GPIO.output(left_motor, GPIO.LOW)
    GPIO.output(right_motor, GPIO.LOW)
    GPIO.output(left_motor_back, GPIO.LOW)
    GPIO.output(right_motor_back, GPIO.LOW)
    print("Sent Command to raspi - move s")

    pass

def move_bot_right():
    GPIO.output(left_motor, GPIO.HIGH)
    GPIO.output(right_motor, GPIO.LOW)
    GPIO.output(left_motor_back, GPIO.LOW)
    GPIO.output(right_motor_back, GPIO.HIGH)
    print("Sent Command to raspi - move r")
    pass

def move_bot_backward():
    GPIO.output(left_motor_back, GPIO.HIGH)
    GPIO.output(right_motor_back, GPIO.HIGH)
    GPIO.output(left_motor, GPIO.LOW)
    GPIO.output(right_motor, GPIO.LOW)
    print("Sent Command to raspi - move b")
    pass

def lights_on():
    print("Inside Lights on")
    pass

def lights_off():
    print("Inside Lights off")
    pass

def uv_on():
    print("Inside UV on")
    pass

def uv_off():
    print("Inside UV off")
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
        motor_speed = value_received
        print(motor_speed)
        return '',204


    else:
        return render_template('additional_settings.html')

@app.route('/additional_settings/<val>')
def additional_settings_action(val):
    if(val=='l1'):
        print("Lights Tasdasun on activated")
        lights_on()
    elif(val=="l0"):
        print("Lights Tuun off activated")
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