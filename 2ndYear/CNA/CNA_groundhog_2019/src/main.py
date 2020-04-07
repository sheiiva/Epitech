#!/usr/bin/env python3
#coding: utf-8

############################################
#                 B-CNA-410                #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#            Project : Groundhog           #
#                                          #
############################################

from sys import argv

from src.checkArgs import ArgumentManager
from src.groundhog import Groundhog
from src.usage import help


def main() -> int:

    argsManager = ArgumentManager()

    if argsManager.needHelp(argv):
        help()
    elif argsManager.checkArgs(argv) == 84:
        return 84
    else:
        groundhog = Groundhog()
        groundhog.run()

if __name__ == "__main__":
    main()
