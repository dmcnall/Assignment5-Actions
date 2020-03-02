import math
from datetime import date 


def firstrun():
    return "success"


def computeArea(r):
    a = r**2 * math.pi
    return a


def firstLastList(newList):
    return newList[0], newList[-1]


def computeDays(d1, d2):
    return abs((d2 - d1).days)
