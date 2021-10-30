import common.graphs as graphs
from copy import deepcopy
import math

def bfs(G, s):
    # Create explored list, queue
    explored = [s]
    Q = [s]
    dist_v = deepcopy(G['nodes'])
    # Record distances
    for key in list(dist_v.keys()):
        dist_v[key] = math.inf
    dist_v[s] = 0
    # Explore all items reachable from s in G
    while len(Q) > 0:
        # Get first item from queue
        v = Q[0]
        del Q[0]
        # Check each incident nodes to see if new nodes available
        for item in G['nodes'][v]:
            edges = G['edges'][item]
            if edges[0] != v:
                w = edges[0]
            else:
                w = edges[1]
            # Mark as explored, add to queue if not explored
            if w not in explored:
                explored.append(w)
                Q.append(w)
                dist_v[w] = dist_v[v]+1
    return explored, dist_v

def compute_undirected_connected_components(G):
    explored = []
    nodes_list = list(G['nodes'].keys())
    for i in range(len(nodes_list)):
        v = nodes_list[i]
        if v not in explored:
            e, dist_v = bfs(G, v)
            print("These are connected nodes {}".format(e))
            explored += e

if __name__ == "__main__":
    # Generate graph
    G = graphs.get_connected_nodes()
    # Compute connected components
    compute_undirected_connected_components(G)
    # BFS basics
    explored, dist_v = bfs(G, 0)
    print("Explored nodes in this order: {}".format(explored))
    print("Shortest path to each node: {}".format(dist_v))