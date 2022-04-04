# Imports
from enum import Enum
import circuits.common as circom
import gates.nor_gate as norg
import gates.not_gate as notg


# Enums
class ConnectTypes(Enum):
    SOURCE = 1
    DRAIN_Q3 = 2
    DRAIN_Q4 = 3
    DRAIN_NOT = 4
    INPUT_A = 5
    INPUT_B = 6
    OUTPUT = 7


# Classes
class OrGate:
    source = None
    drains = None
    input_a = None
    input_b = None
    output = None
    volts = 0

    def __init__(self):
        self.drains = []
        # Create components
        self.nor_gate = norg.NorGate()
        self.not_gate = notg.NotGate()
        # Connect components together
        circom.connect_together(self.nor_gate, self.not_gate, norg.ConnectTypes.OUTPUT, notg.ConnectTypes.INPUT)
        self.circuit = [self.nor_gate, self.not_gate]

    def connect(self, type, obj):
        if type == ConnectTypes.SOURCE:
            self.source = obj
            self.nor_gate.connect(norg.ConnectTypes.SOURCE, obj)
            self.not_gate.connect(notg.ConnectTypes.SOURCE, obj)
        elif type == ConnectTypes.DRAIN_Q3:
            self.drains.append(obj)
            self.nor_gate.connect(norg.ConnectTypes.DRAIN_Q3, obj)
        elif type == ConnectTypes.DRAIN_Q4:
            self.drains.append(obj)
            self.nor_gate.connect(norg.ConnectTypes.DRAIN_Q4, obj)
        elif type == ConnectTypes.DRAIN_NOT:
            self.drains.append(obj)
            self.not_gate.connect(notg.ConnectTypes.DRAIN, obj)
        elif type == ConnectTypes.INPUT_A:
            self.input_a = obj
            self.nor_gate.connect(norg.ConnectTypes.INPUT_A, obj)
        elif type == ConnectTypes.INPUT_B:
            self.input_b = obj
            self.nor_gate.connect(norg.ConnectTypes.INPUT_B, obj)
        elif type == ConnectTypes.OUTPUT:
            self.output = obj
            self.not_gate.connect(notg.ConnectTypes.OUTPUT, obj)

    def simulate(self):
        for component in self.circuit:
            component.simulate()
        self.volts = self.not_gate.volts
