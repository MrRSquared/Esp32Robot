
import time
import machine
"""motor.py: This was designed to work with the Esp 32, Micropython, and an 
L9110s Motor controller, but could probably work with any H bridge style motor interface."""

class go():
    def __init__ (self, Pin_a,Pin_b, invert = False):
        # Set up the motor...
        forward_pin = machine.Pin(Pin_a)
        self.forward_pin = machine.PWM(forward_pin)
        reverse_pin = machine.Pin(Pin_b)
        self.reverse_pin = machine.PWM(reverse_pin)
        
        #just for testing...
        #self.forward_pin = (Pin_a)
        #self.reverse_pin = (Pin_b)
        # Set the PWM frequency
        freq = 50000
        self.forward_pin.freq(freq)
        self.reverse_pin.freq(freq)
        #Invert the motors...
        if invert == True:
            self.invert = -1
        else:
            self.invert = 1
    def drive(self, speed):

        if (speed * self.invert > 1):
            speed = 1
        if (speed * self.invert < -1):
            speed = -1


        if (speed * self.invert >= 0):
            duty_a = int(speed * 1000)
            duty_b = 0
        else:
            duty_a = 0
            duty_b = int(abs(speed) * 1000) 
        self.forward_pin.duty(duty_a)
        self.reverse_pin.duty(duty_b)
        return((duty_a/1000), (duty_b/1000))

left_motor = go(14, 27)
while True:
    print('Moving forward')

    left_motor.drive(.65)
    
    time.sleep(2)
    print('stopping')
    left_motor.drive(0)
    
    time.sleep(2)
    print('Moving in reverse ')
    left_motor.drive(-.75)
    time.sleep(2)
    

