# Imports
import electronics.battery as battery
import electronics.led as led
import electronics.hub_wire as hubwire
import gates.and_gate as and_gate
import circuits.common as circom


# Classes
class AndCircuit:
    circuit = None

    def __init__(self, input1=0, input2=0):
        # Create components
        bat2 = battery.Battery(volts=input1)
        bat3 = battery.Battery(volts=input2)
        ground = battery.Battery(volts=0)
        hub = hubwire.HubWire()
        a = and_gate.AndGate()
        light = led.LED()
        # Connect components together
        circom.connect_together(bat2, a, battery.ConnectTypes.POS, and_gate.ConnectTypes.INPUT_A)
        circom.connect_together(hub, bat2, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)

        circom.connect_together(bat3, a, battery.ConnectTypes.POS, and_gate.ConnectTypes.INPUT_B)
        circom.connect_together(hub, bat3, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)

        circom.connect_together(a, light, and_gate.ConnectTypes.OUTPUT, led.ConnectTypes.SOURCE)
        circom.connect_together(light, ground, led.ConnectTypes.DRAIN, hubwire.ConnectTypes.SOURCES)

        # Add all components of the circuit
        self.circuit = [bat2, bat3, a, light, hub]

    def simulate(self):
        circom.simulate_lightbulb(self, 3)
