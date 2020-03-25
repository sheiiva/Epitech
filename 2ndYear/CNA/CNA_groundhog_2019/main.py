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

from compute import Compute

class Groundhog():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._computer = Compute()
        self._g = None
        self._r = None
        self._s = None
        self._alerts = None
        self._switches = []
        self._values = []
        self._period = int(argv[1])

    def help(self):

        """Show usage of the program."""

        print("SYNOPSIS\n"
                "\t./groundhog period\n\n"
                "DESCRIPTION\n"
                "\tperiod\t\tthe number of days defining a period")

    def getInput(self):

        """
        Wait for user's input and return it if it's a float.
        """

        def isEnd(value):
            if value == "STOP":
                return True
            return False

        try:
            value = input()
            value = float(value)
        except KeyboardInterrupt:
            exit(0)
        except ValueError:
            if isEnd(value):
                return value
            else:
                print("Value must be a float.")
                value = self.getInput()
        else:
            return value

    def outputPrinting(self):

        """
        Print formatted output including:
            * temperature increase average (._g)
            * relative temperature evolution (._r)
            * standard deviation (._s)
            (* alert of switches in global tendency) (._alerts)
        """

        indicators = ["g=", "\t\tr=", "%\t\ts="]
        values = [self._g, self._r, self._s]

        for i in range (0, 3):
            print("{}".format(indicators[i]), end='')
            if values[i] != None and i == 1:
                print("{:d}".format(values[i]), end='')
            elif values[i] != None:
                print("{:.2f}".format(values[i]), end='')
            else:
                print("nan", end='')
        if self._alerts:
            print("\t\ta switch occurs")
        else:
            print("")
        
    def resume(self):
        
        """
        Show a list of the five biggest aberrations observed on the whole time-series
            (sorted by decreasing weird-ness).
        """

        print("Global tendency switched {} times".format(len(self._switches)))
        self._switches.sort()
        self._switches.reverse()
        print("5 weirdest values are {}".format(self._switches[:5]))

    def run(self):

        """
        Run computations and process output printing.
        """

        day = 0
        while True:
            value = self.getInput()
            if (value == "STOP"):
                break
            else:
                self._values.append(value)
                self._computer.process(self, day)
                self.outputPrinting()
            day += 1
        self.resume()
