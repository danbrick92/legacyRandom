# Imports
from enum import Enum


# Enums
class ConnectTypes(Enum):
    SOURCE = 1
    DRAIN = 2


# Classes
class LED:
    source = None
    drain = None
    volts = 0

    def connect(self, type, obj):
        if type == ConnectTypes.SOURCE:
            self.source = obj
        elif type == ConnectTypes.DRAIN:
            self.drain = obj

    def simulate(self):
        self.volts = 1 if self.source.volts > 0 else 0
