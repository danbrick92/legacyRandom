# Imports
import circuits.not_circuit as notc
import circuits.nor_circuit as norc
import circuits.nand_circuit as nandc
import circuits.and_circuit as andc
import circuits.or_circuit as orc
import circuits.basic as basic

# Globals
CIRCUIT = andc.AndCircuit(1, 1)
# CIRCUIT = nandc.NandCircuit(1, 1)
# CIRCUIT = orc.OrCircuit(0, 0)
# CIRCUIT = norc.NorCircuit(0, 0)
# CIRCUIT = notc.NotCircuit(1)
# CIRCUIT = basic.BasicCircuit()

# Functions
if __name__ == "__main__":
    CIRCUIT.simulate()

"""
1) Power gates internally
2) Switch from volts to state (1/0)
"""