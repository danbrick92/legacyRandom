# Imports
import electronics.battery as battery


# Functions
def check_circuit_complete(circuit):
    for start in circuit.circuit:
        # Skip checks for battery
        if isinstance(start, battery.Battery):
            continue
        for i in range(0, 2):
            explored = {}
            nodes = [start]
            while True:
                if len(nodes) <= 0:
                    raise Exception(f"Incomplete Circuit Round {i} Item {start}")
                node = nodes.pop()
                explored[node] = True
                if isinstance(node, battery.Battery):
                    break
                elif node is None:
                    continue
                if i == 0:
                    if 'source' in dir(node) and explored.get(node.source) is None:
                        nodes.append(node.source)
                    elif 'sources' in dir(node):
                        sources = node.sources
                        for source in sources:
                            if explored.get(source) is None:
                                nodes.append(source)
                if i == 1:
                    if 'drain' in dir(node) and explored.get(node.drain) is None:
                        nodes.append(node.drain)
                    elif 'drains' in dir(node):
                        drains = node.drains
                        for drain in drains:
                            if explored.get(drain) is None:
                                nodes.append(drain)


def simulate_lightbulb(circuit, bulb_index):
    # Ensure we have a closed circuit for each component
    check_circuit_complete(circuit)
    # Run the simulation of each component in order
    for component in circuit.circuit:
        component.simulate()
    print(f"Bulb State: {circuit.circuit[bulb_index].volts}")


def connect_together(source, drain, sct, dct):
    source.connect(sct, drain)
    drain.connect(dct, source)
