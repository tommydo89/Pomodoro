
class Timer:

	def __init__(self, minute):
		self.minute = minute
		self.second = 0

	def decrement(self): # decrements the timer by 1 second
		if self.second == 0:
			self.minute -= 1
			self.second = 60
		self.second -= 1

	def reset(self, minute): # resets the timer to a specific minute
		self.minute = minute
		self.second = 0

	def timesUp(self): # returns true if timer has hit 0
		return self.minute == 0 and self.second == 0

	def toStr(self): # returns timer in a string format
		if self.second < 10:
			str_seconds = '0' + str(self.second)
		else:
			str_seconds = str(self.second)
		return str(self.minute) + ":" + str_seconds