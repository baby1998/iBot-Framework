from .. import Command

class Number(Command):
	def __init__(self, number):
		self.value = number

	def run(self):
		print(self.value)