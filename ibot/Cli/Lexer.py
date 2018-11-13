class Lexer:
	def __init__(self, command):
		self.command = command


	def parseStrings(self):
		# linear search. Slow.
		self.strings = []
		i = 0
		start = -1
		for i in range(len(self.command)):
			if self.command[i] in ["'", '"']:
				if (0 < i and '\\' != self.command[i - 1]):
					if(-1 == start):
						start = i
					else:
						self.strings.append(self.command[start + 1:i])
						start = -1
		return self.strings