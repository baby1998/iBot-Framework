import click
import importlib
from .Lexer import Lexer
from .Command import Command
from .ActionCommands import *

def statefulCall():
	# stateful interface to the core
	command = parse(input("> "))
	if isinstance(command, Command):
		# given input is understandable command so run it.
		command.run()
	else:
		if len(command):
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
				if(argument.isnumeric()):
					# make number
					pass
				elif(argument in lexer.strings):
					# use as string
					pass
				else:
					# anything else must be processed as a command again
					parse(argument)

	mod = importlib.import_module('ibot.Cli.ActionCommands.' + lexer.function[0].title())
	return getattr(mod, lexer.function[0].title())()
	try:
		# if len(lexer.arguments):
		# 	# parse operators and solve arguments
		# 	for argument in lexer.arguments:
		# 		# is a number
		# 		if(argument.isnumeric()):
		# 			parse(getattr(importlib.import_module('ibot.Cli.Types.Number'), 'Number')(argument))

		if len(lexer.function):
			# call a function
			mod = importlib.import_module('ibot.Cli.ActionCommands.' + lexer.function[0].title())
			return getattr(mod, lexer.function[0].title())()

		# elif len(lexer.arguments):
		# 	# parse operators and solve arguments
		# 	for argument in lexer.arguments:
		# 		if (argument.isnumeric()):
		# 		# is a number
		# 			return getattr(importlib.import_module('ibot.Cli.Types.Number'), 'Number')(argument)
		# 	pass

	except ImportError:
		return [lexer.function[0] + " is not a valid command."]

	return []
