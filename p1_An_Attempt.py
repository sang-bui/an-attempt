"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"joystick","name":"joystick","typeName":"joystick_one","extraConfig":null,"bufferIndex":0},{"hwid":"5U","name":"b5up","typeName":"joystick_button","extraConfig":null,"bufferIndex":1},{"hwid":"5D","name":"b5down","typeName":"joystick_button","extraConfig":null,"bufferIndex":2},{"hwid":"6U","name":"b6up","typeName":"joystick_button","extraConfig":null,"bufferIndex":3},{"hwid":"6D","name":"b6down","typeName":"joystick_button","extraConfig":null,"bufferIndex":4},{"hwid":"7U","name":"b7up","typeName":"joystick_button","extraConfig":null,"bufferIndex":5},{"hwid":"7D","name":"b7down","typeName":"joystick_button","extraConfig":null,"bufferIndex":6},{"hwid":"7L","name":"b7left","typeName":"joystick_button","extraConfig":null,"bufferIndex":7},{"hwid":"7R","name":"b7right","typeName":"joystick_button","extraConfig":null,"bufferIndex":8},{"hwid":"8U","name":"b8up","typeName":"joystick_button","extraConfig":null,"bufferIndex":9},{"hwid":"8D","name":"b8down","typeName":"joystick_button","extraConfig":null,"bufferIndex":10},{"hwid":"8L","name":"b8left","typeName":"joystick_button","extraConfig":null,"bufferIndex":11},{"hwid":"8R","name":"b8right","typeName":"joystick_button","extraConfig":null,"bufferIndex":12},{"hwid":"Axis1:x","name":"axis1","typeName":"joystick_axis","extraConfig":null,"bufferIndex":13},{"hwid":"Axis2:y","name":"axis2","typeName":"joystick_axis","extraConfig":null,"bufferIndex":14},{"hwid":"Axis3:y","name":"axis3","typeName":"joystick_axis","extraConfig":null,"bufferIndex":15},{"hwid":"Axis4:x","name":"axis4","typeName":"joystick_axis","extraConfig":null,"bufferIndex":16},{"hwid":"AccelX","name":"accelX","typeName":"joystick_axis","extraConfig":null,"bufferIndex":17},{"hwid":"AccelY","name":"accelY","typeName":"joystick_axis","extraConfig":null,"bufferIndex":18}]}"""
# Imports the packages
import sys
import vex

# Defines the joystick
joystick = vex.Joystick()

# Defines all motors
left_motor = vex.Motor(2)
right_motor = vex.Motor(3)
scooper_motor = vex.Motor(4)

# Main loop
def driverMode():
    while True:
        # Assigning joystick mappings for all the motors
        if joystick.b5down():
            right_motor(100)
        elif joystick.b5up():
            right_motor(-100)
        elif joystick.b6down():
            left_motor(100)
        elif joystick.b6up():
            left_motor(-100)
        elif joystick.b8up():
            scooper_motor(100)
        elif joystick.b8right():
            scooper_motor(-100)
        else:
            pass
        # Hit these enter safety mode, use incase of emergency. How do you end up in this situation?
        if joystick.b5down() and joystick.b5up() and joystick.b6down() and joystick.b6up:
            disabledMode()
            break
        else:
            pass

# Disabled Mode is by default, call this in case of an emergency. How do you end up in this situation?
def disabledMode():
    while True:
        left_motor.off()
        right_motor.off()
        scooper_motor.off() 
        print("Disabled mode flag thrown, all motors disabled. Please restart the robot to continue.")
        sys.sleep(5)
        
# We do not have a autonomous feature, place holder for just in case ;)
def autonomousMode():
    pass

# Runs the driver mode in competition mode for you know, competitions.
vex.run_driver(driverMode)