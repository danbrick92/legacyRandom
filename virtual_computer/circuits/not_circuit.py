# Imports
import electronics.battery as battery
import electronics.led as led
import electronics.hub_wire as hubwire
import gates.not_gate as not_gate
import circuits.common as circom


# Classes
class NotCircuit:
    circuit = None

    def __init__(self, input1=0):
        # Create components
        bat = battery.Battery(volts=9)
        bat2 = battery.Battery(volts=input1)
        hub = hubwire.HubWire()
        n = not_gate.NotGate()
        light = led.LED()
        # Connect components together
        circom.connect_together(bat, n, battery.ConnectTypes.POS, not_gate.ConnectTypes.SOURCE)
        circom.connect_together(n, hub, not_gate.ConnectTypes.DRAIN, hubwire.ConnectTypes.SOURCES)
        circom.connect_together(hub, bat, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)
        circom.connect_together(bat2, n, battery.ConnectTypes.POS, not_gate.ConnectTypes.INPUT)
        circom.connect_together(n, light, not_gate.ConnectTypes.OUTPUT, led.ConnectTypes.SOURCE)
        circom.connect_together(light, hub, led.ConnectTypes.DRAIN, hubwire.ConnectTypes.SOURCES)
        # Add all components of the circuit
        self.circuit = [bat, bat2, hub, n, light]

    def simulate(self):
        circom.simulate_lightbulb(self, 4)
