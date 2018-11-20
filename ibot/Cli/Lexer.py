class Lexer:
	def __init__(self, command):
		self.command = command


	def parseStrings(self):
		# parses strings in command
		self.strings = []		# Todo: Replace with linked list
		i = 0
		start = -1
		quote = ["'", '"']

		# linear search. O(n)
		for i in range(len(self.command)):
			if self.command[i] in quote:
				if (0 < i and '\\' != self.command[i - 1]):
					if(-1 == start):
						start = i
						quote = [self.command[i]]
					else:
						self.strings.append(self.command[start + 1:i])
						start = -1
						quote = ["'", '"']
		return self.strings


	def parseArgs(self):
		# parses arguments for functions in command. Assumes strings are parsed
		command = self.command
		strings = self.strings
		for i in range(len(strings)):
			command.replace(strings[i], "%" + str(i) + "%")

		arguments = command.split(" ")[1:] # everything is an argument except first word

		# restore strings at appropriate places
		def restoreStrings(x):
			if (x[0] == '%' and x[len(x)] == '%'):
				i = x.replace("%", "")
				if(isnumeric(i)):
					return strings[i]
			return x
		self.arguments = list(map(restoreStrings, arguments))

		return self.arguments


	def parseFunc(self):
		#parses functions in command. Assumes functions to be already parsed
		command = self.command
		strings = self.strings

		for string in strings:
			command.replace(string, "|")

		self.function = [command.split(" ")[0]] # first word is always a function.
		return self.function


	def parse(self):
		self.parseStrings()
		self.parseArgs()
		self.parseFunc()
		return self
