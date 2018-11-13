#!/usr/bin/env python

import ibot.Cli

if (__name__ == '__main__'):
    try:
        cli = Cli()
        while(True):
            ibot.cli.parse(input("> "))
    except KeyboardInterrupt:
        exit()
