# Imports
from enum import Enum
import transistors.n_transistor as n_type
import transistors.p_transistor as p_type
import circuits.common as circom
import electronics.hub_wire as hubwire


# Enums
class ConnectTypes(Enum):
    SOURCE = 1
    DRAIN_Q3 = 2
    DRAIN_Q4 = 3
    INPUT_A = 4
    INPUT_B = 5
    OUTPUT = 6


# Classes
class NorGate:
    source = None
    drains = None
    input_a = None
    input_b = None
    output = None
    volts = 0

    def __init__(self):
        self.drains = []
        # Create components
        self.input_a_hub = hubwire.HubWire()
        self.input_b_hub = hubwire.HubWire()
        self.output_hub = hubwire.HubWire()
        self.q1 = p_type.PTransistor()
        self.q2 = p_type.PTransistor()
        self.q3 = n_type.NTransistor()
        self.q4 = n_type.NTransistor()
        # Connect components together
        circom.connect_together(self.q1, self.q2, p_type.ConnectTypes.DRAIN, p_type.ConnectTypes.SOURCE)
        circom.connect_together(self.q2, self.output_hub, p_type.ConnectTypes.DRAIN, hubwire.ConnectTypes.SOURCES)
        circom.connect_together(self.q3, self.output_hub, n_type.ConnectTypes.DRAIN, hubwire.ConnectTypes.SOURCES)
        circom.connect_together(self.q4, self.output_hub, n_type.ConnectTypes.DRAIN, hubwire.ConnectTypes.SOURCES)

        circom.connect_together(self.input_a_hub, self.q1, hubwire.ConnectTypes.DRAINS, p_type.ConnectTypes.GATE)
        circom.connect_together(self.input_a_hub, self.q3, hubwire.ConnectTypes.DRAINS, n_type.ConnectTypes.GATE)
        circom.connect_together(self.input_b_hub, self.q2, hubwire.ConnectTypes.DRAINS, p_type.ConnectTypes.GATE)
        circom.connect_together(self.input_b_hub, self.q4, hubwire.ConnectTypes.DRAINS, n_type.ConnectTypes.GATE)

        self.circuit = [self.input_a_hub, self.input_b_hub, self.q1, self.q2, self.q3, self.q4, self.output_hub]

    def connect(self, type, obj):
        if type == ConnectTypes.SOURCE:
            self.source = obj
            self.q1.connect(p_type.ConnectTypes.SOURCE, obj)
        elif type == ConnectTypes.DRAIN_Q3:
            self.drains.append(obj)
            self.q3.connect(n_type.ConnectTypes.SOURCE, obj)
        elif type == ConnectTypes.DRAIN_Q4:
            self.drains.append(obj)
            self.q4.connect(n_type.ConnectTypes.SOURCE, obj)
        elif type == ConnectTypes.INPUT_A:
            self.input_a = obj
            self.input_a_hub.connect(hubwire.ConnectTypes.SOURCES, obj)
        elif type == ConnectTypes.INPUT_B:
            self.input_b = obj
            self.input_b_hub.connect(hubwire.ConnectTypes.SOURCES, obj)
        elif type == ConnectTypes.OUTPUT:
            self.output = obj
            self.output_hub.connect(hubwire.ConnectTypes.DRAINS, obj)

    def simulate(self):
        for component in self.circuit:
            component.simulate()
        self.volts = self.output_hub.volts
