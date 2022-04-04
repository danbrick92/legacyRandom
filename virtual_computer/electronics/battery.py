# Imports
from enum import Enum


# Enums
class ConnectTypes(Enum):
    POS = 1
    NEG = 2


# Classes
class Battery:
    pos = None
    neg = None
    volts = 0

    def __init__(self, volts):
        self.volts = volts

    def connect(self, type, obj):
        if type == ConnectTypes.POS:
            self.pos = obj
        elif type == ConnectTypes.NEG:
            self.neg = obj

    def simulate(self):
        pass
