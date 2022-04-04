# Imports
from enum import Enum


# Enums
class ConnectTypes(Enum):
    SOURCE = 1
    DRAIN = 2
    GATE = 3


# Classes
class NTransistor:
    source = None
    drain = None
    gate = None
    volts = 0

    def connect(self, type, obj):
        if type == ConnectTypes.SOURCE:
            self.source = obj
        elif type == ConnectTypes.DRAIN:
            self.drain = obj
        elif type == ConnectTypes.GATE:
            self.gate = obj

    def simulate(self):
        multiplier = 1 if self.gate.volts > 0 else 0
        self.volts = multiplier * self.source.volts
