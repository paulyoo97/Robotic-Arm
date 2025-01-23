### ROBOTIC ARM CONTROL APP
# Uses Python to communicate with Arduino Board and control motors.
# Note - remember to upload the StandardFirmata sketch onto the board before running this script.
# In Arduino IDE > File > Examples > Firmata > StandardFirmata, change Firmata.begin(57600) to Firmata.begin(9600)Rate is 9600.

### Libraries for Electronics
from pyfirmata import Arduino, SERVO
import time

### Set up board
board = Arduino('COM4')

### Set up motors
# Stepper motor
stepper_motor = board.get_pin('d:3:p')    # sets the steps of the stepper motor.
motor_direction = board.get_pin('d:4:o')    # sets the direction of rotation of the stepper motor.

# Servo motors
servo1 = board.digital[5]
servo1.mode = SERVO

servo2 = board.digital[6]
servo2.mode = SERVO

servo3 = board.digital[9]
servo3.mode = SERVO

servo4 = board.digital[10]
servo4.mode = SERVO

servo5 = board.digital[11]
servo5.mode = SERVO


### Library for GUI
import tkinter as tk
import tkinter.messagebox
import customtkinter

# Appearance and colour scheme
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# Set up the main window
app = customtkinter.CTk()
app.geometry('400x400')
app.title('Robotic Arm Control')
label = customtkinter.CTkLabel(master=app, text='Robotic Arm Control',font=('Roboto',20))
label.pack(padx=10, pady=10, fill='both')


### Create Functions
# Function for Stepper Motor
initial = 0
def stepper_rotation(slider):
    global initial
    final = int(float(slider.get()))
    # Determine the direction
    if (final- initial) > 0:
        motor_direction.write(1)    # clockwise direction
        direction = 'Clockwise'
    elif (final - initial) <= 0:
        motor_direction.write(0)    # counter clockwise direction
        direction = 'Counter Clockwise'
    # Determine the number of steps to change from initial position to desired final position
    steps = abs(final - initial)
    print(f'''
          Direction: {direction}
          Steps: {steps}
          Final Position {final}''')
    
    for step in range(steps):
        stepper_motor.write(1)
        stepper_motor.write(0)
    
    initial = final # This variable is used reference position for next direction


# Functions for Servos
def rotate(motor,angle):
    motor.write(int(float(angle)))

def slider_command(slider,motor):
    angle = slider.get()
    rotate(motor, angle)


### Motor Controls
titleframe = customtkinter.CTkFrame(master=app,fg_color='gray10')
titleframe.pack(side='left',expand=True, fill='both')
sliderframe = customtkinter.CTkFrame(master=app,fg_color='gray10')
sliderframe.pack(side='left',expand=True,fill='both')

# Stepper Motor
customtkinter.CTkLabel(master=titleframe, text='Stepper Motor',font=('Roboto',14)).pack(padx=10, pady=10)
sm = customtkinter.CTkSlider(master=sliderframe,from_=-100, to=100,command=lambda _:stepper_rotation(sm))   #    100 steps = 180 degrees.
sm.pack(padx=15, pady=15)


# Servo 1
customtkinter.CTkLabel(master=titleframe, text='Servo 1',font=('Roboto',14)).pack(padx=10, pady=10)
s1 = customtkinter.CTkSlider(master=sliderframe,from_=0, to=180,command=lambda _:slider_command(s1,servo1))   # Takes current value as the argument "angle"
s1.set(0)
s1.pack(padx=15, pady=15)

# Servo 2
customtkinter.CTkLabel(master=titleframe, text='Servo 2',font=('Roboto',14)).pack(padx=10, pady=10)
s2 = customtkinter.CTkSlider(master=sliderframe,from_=0, to=180,command=lambda _:slider_command(s2,servo2))   # Takes current value as the argument "angle"
s2.set(0)
s2.pack(padx=15, pady=15)

# Servo 3
customtkinter.CTkLabel(master=titleframe, text='Servo 3',font=('Roboto',14)).pack(padx=10, pady=10)
s3 = customtkinter.CTkSlider(master=sliderframe,from_=0, to=180,command=lambda _:slider_command(s3,servo3))   # Takes current value as the argument "angle"
s3.set(0)
s3.pack(padx=15, pady=15)

# Servo 4
customtkinter.CTkLabel(master=titleframe, text='Servo 4',font=('Roboto',14)).pack(padx=10, pady=10)
s4 = customtkinter.CTkSlider(master=sliderframe,from_=0, to=180,command=lambda _:slider_command(s4,servo4))   # Takes current value as the argument "angle"
s4.set(0)
s4.pack(padx=15, pady=15)

# Servo 5
customtkinter.CTkLabel(master=titleframe, text='Servo 5',font=('Roboto',14)).pack(padx=10, pady=10)
s5 = customtkinter.CTkSlider(master=sliderframe,from_=0, to=90,command=lambda _:slider_command(s5,servo5))   # Takes current value as the argument "angle"
s5.set(0)
s5.pack(padx=15, pady=15)   ### remove servo motor and adjust to the correct orientation.

app.mainloop()