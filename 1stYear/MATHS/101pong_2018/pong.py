#!/usr/bin/env python3
#coding: utf-8

############################################
#                MATHEMATICS               #
############################################
#                                          #
#       Verlhac Lilian & ROZET Corentin    #
#                                          #
#           Project : 101pong_2018         #
#                                          #
############################################

from sys import argv
from math import sqrt, fabs, degrees, atan, pow

class Pong():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self.x0 = float(argv[1])
        self.y0 = float(argv[2])
        self.z0 = float(argv[3])
        self.x1 = float(argv[4])
        self.y1 = float(argv[5])
        self.z1 = float(argv[6])
        self.n = float(argv[7])
        self.xt = 0
        self.yt = 0
        self.zt = 0
        self.xd = 0
        self.yd = 0
        self.zd = 0
        self.norm = 0

    def compute(self):

        """
        Run computation of input values.
        """

        self.xt = self.x1 - self.x0
        self.yt = self.y1 - self.y0
        self.zt = self.z1 - self.z0
        self.xd = str("%.2f" % float(self.xt * self.n + self.x1))
        self.yd = str("%.2f" % float(self.yt * self.n + self.y1))
        self.zd = str("%.2f" % float(self.zt * self.n + self.z1))
        self.norm = sqrt(pow(self.xt, 2) + (pow(self.yt, 2)))

        if self.norm != 0:
            return str("%.2f" % float(fabs(degrees(atan(self.zt / self.norm)))))
        else:
            return str("%.2f" % 90)

    def print(self, angle):

        """
        Run printing of computed values.
        """

        x = str("%.2f" % self.xt)
        y = str("%.2f" % self.yt)
        z = str("%.2f" % self.zt)

        print("The velocity vector of the ball is:\n"
        '('+x+', '+y+', '+z+')\n'
        'At time t + '+argv[7]+', ball coordinates will be:\n'
        '('+self.xd+', '+self.yd+', '+self.zd+')')

        if self.zt > 0 or (self.zt == 0 and self.z0 != 0):
            print("The ball won’t reach the bat.")
        else :
            print("The incidence angle is:\n"
                    +angle+" degrees")

        return 0
