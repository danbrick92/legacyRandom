# Imports
import circuits.not_circuit as notc
import circuits.nor_circuit as norc
import circuits.or_circuit as orc
import circuits.basic as basic

# Globals
CIRCUIT = orc.OrCircuit(0, 0)
#CIRCUIT = norc.NorCircuit(0, 0)
# CIRCUIT = notc.NotCircuit(1)
# CIRCUIT = basic.BasicCircuit()

# Functions
if __name__ == "__main__":
    CIRCUIT.simulate()


"""
TODO: 
-Implementation does not allow multiple connections
"""
