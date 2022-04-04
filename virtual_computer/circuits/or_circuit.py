# Imports
import electronics.battery as battery
import electronics.led as led
import electronics.hub_wire as hubwire
import gates.or_gate as or_gate
import circuits.common as circom


# Classes
class OrCircuit:
    circuit = None

    def __init__(self, input1=0, input2=0):
        # Create components
        bat = battery.Battery(volts=9)
        bat2 = battery.Battery(volts=input1)
        bat3 = battery.Battery(volts=input2)
        ground = battery.Battery(volts=0)
        hub = hubwire.HubWire()
        o = or_gate.OrGate()
        light = led.LED()
        # Connect components together
        circom.connect_together(bat, o, battery.ConnectTypes.POS, or_gate.ConnectTypes.SOURCE)
        circom.connect_together(light, hub, led.ConnectTypes.DRAIN, hubwire.ConnectTypes.SOURCES)
        circom.connect_together(hub, bat, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)

        circom.connect_together(bat2, o, battery.ConnectTypes.POS, or_gate.ConnectTypes.INPUT_A)
        circom.connect_together(hub, bat2, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)

        circom.connect_together(bat3, o, battery.ConnectTypes.POS, or_gate.ConnectTypes.INPUT_B)
        circom.connect_together(hub, bat3, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)

        circom.connect_together(o, light, or_gate.ConnectTypes.OUTPUT, led.ConnectTypes.SOURCE)

        circom.connect_together(ground, o, battery.ConnectTypes.POS, or_gate.ConnectTypes.DRAIN_Q3)
        circom.connect_together(ground, o, battery.ConnectTypes.POS, or_gate.ConnectTypes.DRAIN_Q4)
        circom.connect_together(ground, o, battery.ConnectTypes.POS, or_gate.ConnectTypes.DRAIN_NOT)

        # Add all components of the circuit
        self.circuit = [bat, bat2, bat3, o, light, hub]

    def simulate(self):
        circom.simulate_lightbulb(self, 4)
