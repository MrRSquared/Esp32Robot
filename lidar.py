import time
from machine import I2C

'''Description of our sensor...
Upgraded version
Increase the cover to prevent dust
Application
High speed auto focus
Video continuous autofocus
User detection of computers and other devices
Obstacle detection
Automatic recognition of gestures of white goods (such as faucets, refrigerators, etc.)
Parameter
Measuring range Ranging Range 100 ~ 1800mm
Working voltage VCC 3 ~ 5V
Working current ICC_VDD 35mA
Working temperature Topr - 20 + 70 °C
Storage temperature Tstg - 40 + 85 °C
Communication protocol
Baud rate Bits per Second: 9600
Data Bits Data Bits : 8
Parity None Parity : None
Stop bits Stop bits : 1
Flow Control Flow Control : Non'''

i2c = I2C(freq= 9600)

i2c.scan()
while True:
    try:
        distance = i2c.readfrom(164, 8) 
        print(float(distance))
    raise:
        except

