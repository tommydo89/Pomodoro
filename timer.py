
class Timer:

	def __init__(self, minute):
		self.minute = minute
		self.second = 0

	def decrement(self):
		if self.second == 0:
			self.minute -= 1
			self.second = 60
		self.second -= 1

	def reset(self, minute):
		self.minute = minute
		self.second = 0

	def timesUp(self):
		return self.minute == 0 and self.second == 0

	def toStr(self):
		if self.second < 10:
			str_seconds = '0' + str(self.second)
		else:
			str_seconds = str(self.second)
		return str(self.minute) + ":" + str_seconds