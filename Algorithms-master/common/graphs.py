# Creates seperate clusters of connected nodes that do not have crossing lines
def get_disconnected_nodes():
    nodes = {
        1: [0, 1],
        2: [5],
        3: [2, 0],
        4: [5],
        5: [3, 4, 1, 2],
        6: [6, 7],
        7: [3],
        8: [8, 6],
        9: [4],
        10: [7, 8]
    }
    edges = {
        0: (1, 3),
        1: (1, 5),
        2: (3, 5),
        3: (5, 7),
        4: (5, 9),
        5: (2, 4),
        6: (6, 8),
        7: (6, 10),
        8: (8, 10)
    }
    return { 'nodes' : nodes, 'edges' : edges}

# Creates a single cluster of connected nodes
def get_connected_nodes():
    nodes = {
        0: [0, 1],
        1: [0, 2],
        2: [1, 4, 6],
        3: [3, 5, 6],
        4: [4, 5, 7],
        5: [3, 7]
    }
    edges = {
        0: (0, 1),
        1: (0, 2),
        2: (1, 3),
        3: (3, 5),
        4: (2, 4),
        5: (3, 4),
        6: (2, 3),
        7: (4, 5)
    }
    return {'nodes': nodes, 'edges': edges}

# Gets a directed graph
def get_directed_graph():
    nodes = {
        0: [0, 1],
        1: [2],
        2: [3, 4],
        3: [5],
        4: [6],
        5: [7],
        6: []
    }
    edges = {
        0: (0, 1),
        1: (0, 2),
        2: (1, 3),
        3: (2, 4),
        4: (2, 5),
        5: (3, 4),
        6: (4, 5),
        7: (5, 6)
    }
    return {'nodes': nodes, 'edges': edges}

# Gets a directed graph
def get_scc_graph():
    nodes = {
        1: [0],
        2: [9],
        3: [6],
        4: [1],
        5: [10],
        6: [5, 7],
        7: [2, 3],
        8: [8],
        9: [4]
    }
    edges = {
        0: (1,7),
        1: (4,1),
        2: (7,4),
        3: (7,9),
        4: (9,6),
        5: (6,3),
        6: (3,9),
        7: (6,8),
        8: (8,2),
        9: (2,5),
        10: (5,8)
    }
    return {'nodes': nodes, 'edges': edges}

def reverse_graph_in_place(G):
    edges = list(G['edges'].keys())
    for edge in edges:
        e = G['edges'][edge]
        if edge not in G['nodes'][e[0]]:
            G['nodes'][e[0]].append(edge)
            G['nodes'][e[1]].remove(edge)
        else:
            G['nodes'][e[1]].append(edge)
            G['nodes'][e[0]].remove(edge)
    return G