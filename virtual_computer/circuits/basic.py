# Imports
import electronics.battery as battery
import electronics.led as led
import transistors.n_transistor as n_type
import transistors.p_transistor as p_type
import circuits.common as circom


# Classes
class BasicCircuit:
    circuit = None

    def __init__(self):
        # Create components
        bat = battery.Battery(volts=9)
        bat2 = battery.Battery(volts=9)
        n = n_type.NTransistor()
        light = led.LED()
        # Connect components together
        circom.connect_together(bat, n, battery.ConnectTypes.POS, n_type.ConnectTypes.SOURCE)
        circom.connect_together(n, light, n_type.ConnectTypes.DRAIN, led.ConnectTypes.SOURCE)
        circom.connect_together(light, bat, led.ConnectTypes.DRAIN, battery.ConnectTypes.NEG)
        circom.connect_together(bat2, n, battery.ConnectTypes.POS, n_type.ConnectTypes.GATE)
        # Add all components of the circuit
        self.circuit = [bat, n, light, bat2]

    def simulate(self):
        circom.simulate_lightbulb(self, 2)
