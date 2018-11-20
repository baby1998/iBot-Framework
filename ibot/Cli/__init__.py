import click
import importlib
from .Lexer import Lexer
from .Command import Command
from .Types.Number import Number
# from .ActionCommands import *

def statefulCall():
	# stateful interface to the core
	command = parse(input("> "))
	if isinstance(command, Command):
		# given input is understandable command so run it.
		command.run()
	else:
		if command:
			print(command[0])
    

def statelessCall():
	# stateless interface to the core
	# do click stuff here.
	pass


def parse(command):
	if(isinstance(command, Command)):
		# understandable command, no need of parsing
		return command

	# parse the command
	lexer = Lexer(command).parse()
	if len(lexer.function):
		if len(lexer.arguments):
			for argument in lexer.arguments:
				newCommand = parse(argument)
				if(isinstance(newCommand, Command)):
					newCommand.run()

		if(lexer.function[0].isnumeric()):
			return Number(lexer.function[0])

		elif(lexer.function[0] in lexer.strings):
			return String(lexer.function[0])

		# else:
		# 	if(isinstance(newCommand, Command)):
		# 		newCommand.run()
		# 	# anything else must be processed as a command again
		# 	newCommand = parse(lexer.function[0])

	if lexer.function:
		try:
			mod = importlib.import_module('ibot.Cli.ActionCommands.' + lexer.function[0].title())
			return getattr(mod, lexer.function[0].title())()
		except ImportError:
			return [lexer.function[0] + " is not a valid command."]
		return []
