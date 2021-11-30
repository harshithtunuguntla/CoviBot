from flask import Flask, render_template, request, redirect, Response

app = Flask(__name__)



def move_bot_forward():
    print("Sent Command to raspi - move f")
    pass

def move_bot_left():
    print("Sent Command to raspi - move l")
    pass

def move_bot_stop():
    print("Sent Command to raspi - move s")
    pass

def move_bot_right():
    print("Sent Command to raspi - move r")
    pass

def move_bot_backward():
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