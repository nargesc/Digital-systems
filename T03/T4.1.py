# Variables representing the state of the sensors
L = False
C = False
R = False

def full_speed():
    print("Robot is running at full speed!")

if not (L or C or R):
    full_speed()
