# Imports
from enum import Enum
import transistors.n_transistor as n_type
import transistors.p_transistor as p_type
import circuits.common as circom


# Enums
class ConnectTypes(Enum):
    SOURCE = 1
    DRAIN = 2
    INPUT = 3
    OUTPUT = 4


# Classes
class NotGate:
    source = None
    drain = None
    input = None
    output = None
    p = None
    n = None
    circuit = None
    volts = 0

    def __init__(self):
        # Create components
        self.n = n_type.NTransistor()
        self.p = p_type.PTransistor()
        # Connect components together
        circom.connect_together(self.p, self.n, p_type.ConnectTypes.DRAIN, n_type.ConnectTypes.SOURCE)
        # Set components
        self.circuit = [self.p, self.n]

    def connect(self, type, obj):
        if type == ConnectTypes.SOURCE:
            self.source = obj
            self.p.connect(p_type.ConnectTypes.SOURCE, obj)
        elif type == ConnectTypes.DRAIN:
            self.drain = obj
            self.n.connect(n_type.ConnectTypes.DRAIN, obj)
        elif type == ConnectTypes.INPUT:
            self.input = obj
            self.p.connect(p_type.ConnectTypes.GATE, obj)
            self.n.connect(n_type.ConnectTypes.GATE, obj)
        elif type == ConnectTypes.OUTPUT:
            self.output = obj

    def simulate(self):
        for component in self.circuit:
            component.simulate()
        self.volts = max(self.n.volts, self.p.volts)
