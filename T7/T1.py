from machine import Pin
import utime

# Define button and lamp
btn = Pin(7, Pin.IN, Pin.PULL_UP)  # SW2 button with internal pull-up resistor
lamp = Pin(20, Pin.OUT)  # LED3 as an output

# Define state machine states
OFF = 0  # Lamp is OFF
ONW = 1  # Lamp is ON - Waiting for button release
ON = 2  # Lamp is ON
OFFW = 3  # Lamp is OFF - Waiting for button release

# Initialize state
state = OFF

# Set clock period (50ms = 20Hz)
clock_period = 50

while True:
    if state == OFF:
        lamp.value(0)  # Turn off the lamp
        if btn.value() == 0:  # If the button is pressed
            state = ONW  # Transition to ONW state

    elif state == ONW:
        lamp.value(1)  # Turn on the lamp
        if btn.value() == 1:  # If the button is released
            state = ON  # Transition to ON state

    elif state == ON:
        if btn.value() == 0:  # If the button is pressed again
            state = OFFW  # Transition to OFFW state

    elif state == OFFW:
        lamp.value(0)  # Turn off the lamp
        if btn.value() == 1:  # If the button is released
            state = OFF  # Return to OFF state

    utime.sleep_ms(clock_period)  # Maintain the state machine clock timing

