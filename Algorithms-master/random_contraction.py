import random
import math
from copy import deepcopy

def get_len_dict(x):
    return len(list(x.keys()))

def min_cut(V,E):
    while get_len_dict(V) > 2:
        # Pick remaining edge at random
        r = random.randint(0, get_len_dict(E)-1)
        # Grab edge of interest
        e_keys_list = list(E.keys())
        edge = E[e_keys_list[r]]
        # Merge into single vertex
        e_abs = V[edge[1]] # Get edges of vertex that will be absorbed
        # Rewrite edges to point to new super node
        for e in e_abs:
            b = E[e]
            if b[0] == edge[1]:
                b = (edge[0], b[1])
            if b[1] == edge[1]:
                b = (b[0], edge[0])
            E[e] = b
        # Record #s, Remove node
        e_sup = list(set(V[edge[0]] + V[edge[1]]))
        del V[edge[1]]
        # Remove self-loops, records of those in V
        new_edges = []
        for e in e_sup:
            b = E[e]
            if b[0] == b[1]:
                del E[e]
            else:
                new_edges.append(e)
        V[edge[0]] = new_edges
    return len(list(E.keys()))

def random_contraction(V,E):
    len_v = get_len_dict(V)
    t = int(math.log(len_v * len_v**2))
    mc_min = 10000000000000000000
    for i in range(t):
        v = deepcopy(V)
        e = deepcopy(E)
        mc = min_cut(v, e)
        if mc < mc_min:
            mc_min = mc
    return mc_min

if __name__ == "__main__":
    nodes = {
        0: [0, 3],
        1: [0, 1, 4],
        2: [3, 2, 4],
        3: [1, 2]
    }
    edges = {
        0: (0, 1),
        1: (1, 3),
        2: (3, 2),
        3: (0, 2),
        4: (2, 1)
    }
    mc = random_contraction(nodes,edges)
    print("Min Cut: {}".format(mc))