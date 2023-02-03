# Imports
from enum import Enum
import circuits.common as circom
import gates.nand_gate as nandg
import gates.not_gate as notg
import electronics.battery as battery
import electronics.hub_wire as hubwire


# Enums
class ConnectTypes(Enum):
    INPUT_A = 1
    INPUT_B = 2
    OUTPUT = 3


# Classes
class AndGate:
    input_a = None
    input_b = None
    output = None
    volts = 0

    def __init__(self):
        self.drains = []
        # Create components
        self.nand_gate = nandg.NandGate()
        self.not_gate = notg.NotGate()
        # Connect components together
        circom.connect_together(self.nand_gate, self.not_gate, nandg.ConnectTypes.OUTPUT, notg.ConnectTypes.INPUT)
        self.self_power()
        self.circuit = [self.bat, self.hub, self.bat2, self.hub2, self.nand_gate, self.not_gate]

    def self_power(self):
        self.bat = battery.Battery(volts=9)
        self.hub = hubwire.HubWire()
        self.bat2 = battery.Battery(volts=0)
        self.hub2 = hubwire.HubWire()
        # Power sources
        circom.connect_together(self.bat, self.hub, battery.ConnectTypes.POS, hubwire.ConnectTypes.SOURCES)
        circom.connect_together(self.hub, self.nand_gate, hubwire.ConnectTypes.DRAINS, nandg.ConnectTypes.SOURCE)
        circom.connect_together(self.hub, self.not_gate, hubwire.ConnectTypes.DRAINS, notg.ConnectTypes.SOURCE)
        # Connect drains
        circom.connect_together(self.bat2, self.hub2, battery.ConnectTypes.POS, hubwire.ConnectTypes.SOURCES)
        circom.connect_together(self.hub2, self.nand_gate, hubwire.ConnectTypes.DRAINS, nandg.ConnectTypes.DRAIN)
        circom.connect_together(self.hub2, self.not_gate, hubwire.ConnectTypes.DRAINS, notg.ConnectTypes.DRAIN)
        # Ground batteries
        circom.connect_together(self.hub2, self.bat, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)
        circom.connect_together(self.hub2, self.bat2, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)

    def connect(self, type, obj):
        if type == ConnectTypes.INPUT_A:
            self.input_a = obj
            self.nand_gate.connect(nandg.ConnectTypes.INPUT_A, obj)
        elif type == ConnectTypes.INPUT_B:
            self.input_b = obj
            self.nand_gate.connect(nandg.ConnectTypes.INPUT_B, obj)
        elif type == ConnectTypes.OUTPUT:
            self.output = obj
            self.not_gate.connect(notg.ConnectTypes.OUTPUT, obj)

    def simulate(self):
        for component in self.circuit:
            component.simulate()
        self.volts = self.not_gate.volts
