# Imports
from enum import Enum


# Enums
class ConnectTypes(Enum):
    SOURCES = 1
    DRAINS = 2


# Classes
class HubWire:
    sources = None
    drains = None
    volts = 0

    def __init__(self):
        self.sources = []
        self.drains = []

    def connect(self, type, obj):
        if type == ConnectTypes.SOURCES:
            self.sources.append(obj)
        elif type == ConnectTypes.DRAINS:
            self.drains.append(obj)

    def simulate(self):
        self.volts = 0
        for source in self.sources:
            self.volts += source.volts
