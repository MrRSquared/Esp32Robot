class go():
	def  __init__ (self, Pin_a, Pin_b, type, invert = False):
		self.Pin_a = Pin_a
		self.Pin_b = Pin_b
		self.type = type
		self.invert = invert
		if (self.type == 'tt'):
			freq = 3500
		elif (self.type == 'vex'):
			freq = 2200
		print(freq)
	def drive(self, speed):
		if (speed >= 0):
			duty_a = speed * 1000
			duty_b = 0
		else:
			duty_a = 0
			duty_b = abs(speed)*1000
		return (duty_a, duty_b)
			
		
		
left_motor = go(2, 3, 'tt')
right_motor =go(4, 5, 'vex')
stuff =right_motor.drive(-1)
print(stuff)
