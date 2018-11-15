#!/usr/bin/env python

from ibot import Cli
import sys

if (__name__ == '__main__'):
    try:
        if(len(sys.argv) > 1):
        	# Cli 
        	Cli.statelessCall()
        	exit()

        # REPL
        while(True):
        	Cli.statefulCall()

    except KeyboardInterrupt:
        exit()
