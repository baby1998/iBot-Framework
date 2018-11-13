import click
import importlib
from .Lexer import Lexer
from .Command import Command

def statefulCall():
	command = parse(input("> "))
	if isinstance(command, Command):
		# given input is understandable command so run it.
		command.run()
	
	# stateful interface to the core
    

def statelessCall():
	# stateless interface to the core
	# do click stuff here.
	pass	

def parse(command):
	lexer = Lexer(command)
	lexer.parseStrings()
	print(lexer.strings)
	# importlib.import_module('Cli' + lexer['order'])
	# return Command() # returns an understandable command object