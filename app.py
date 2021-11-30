from flask import Flask, render_template, request, redirect, Response
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)


app = Flask(__name__)

left_motor = 4
right_motor = 25

left_motor_back = 11
right_motor_back = 12


GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor, GPIO.OUT)
GPIO.setup(right_motor, GPIO.OUT)
GPIO.setup(left_motor_back, GPIO.OUT)
GPIO.setup(right_motor_back, GPIO.OUT)



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
    GPIO.output(left_motor_back, GPIO.LOW)
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
    GPIO.output(right_motor_back, GPIO.LOW)
    print("Sent Command to raspi - move r")
    pass

def move_bot_backward():
    GPIO.output(left_motor_back, GPIO.HIGH)
    GPIO.output(right_motor_back, GPIO.HIGH)
    GPIO.output(left_motor, GPIO.LOW)
    GPIO.output(right_motor, GPIO.LOW)
    print("Sent Command to raspi - move b")
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


if __name__ == '__main__':
    app.run(debug=True)