# Imports
import electronics.battery as battery
import electronics.led as led
import electronics.hub_wire as hubwire
import gates.nand_gate as nand_gate
import circuits.common as circom


# Classes
class NandCircuit:
    circuit = None

    def __init__(self, input1=0, input2=0):
        # Create components
        bat = battery.Battery(volts=9)
        bat2 = battery.Battery(volts=input1)
        bat3 = battery.Battery(volts=input2)
        ground = battery.Battery(volts=0)
        hub = hubwire.HubWire()
        n = nand_gate.NandGate()
        light = led.LED()
        # Connect components together
        circom.connect_together(bat, n, battery.ConnectTypes.POS, nand_gate.ConnectTypes.SOURCE)
        circom.connect_together(light, hub, led.ConnectTypes.DRAIN, hubwire.ConnectTypes.SOURCES)
        circom.connect_together(hub, bat, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)

        circom.connect_together(bat2, n, battery.ConnectTypes.POS, nand_gate.ConnectTypes.INPUT_A)
        circom.connect_together(hub, bat2, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)

        circom.connect_together(bat3, n, battery.ConnectTypes.POS, nand_gate.ConnectTypes.INPUT_B)
        circom.connect_together(hub, bat3, hubwire.ConnectTypes.DRAINS, battery.ConnectTypes.NEG)

        circom.connect_together(n, light, nand_gate.ConnectTypes.OUTPUT, led.ConnectTypes.SOURCE)

        circom.connect_together(ground, n, battery.ConnectTypes.POS, nand_gate.ConnectTypes.DRAIN)

        # Add all components of the circuit
        self.circuit = [bat, bat2, bat3, n, light, hub]

    def simulate(self):
        circom.simulate_lightbulb(self, 4)
