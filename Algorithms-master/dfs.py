import common.graphs as graphs
from copy import deepcopy

# Globals
order_index = -1
ordering = {}
finishing_time = {}
cur_fin = -1
leaders = {}
cur_leader = -1
record_finishing_times = True

def dfs(G, s, explored=[]):
    # Pull in globals
    global order_index
    global ordering
    global finishing_time
    global leaders
    global cur_fin
    # Create explored list, queue
    explored.append(s)
    leaders[s] = cur_leader
    for item in G['nodes'][s]:
        edges = G['edges'][item]
        if edges[0] != s:
            v = edges[0]
        else:
            v = edges[1]
        if v not in explored:
            explored = dfs(G, v, explored)
    # Record topological order
    ordering[s] = order_index
    order_index -= 1
    # Record scc data
    cur_fin += 1
    if record_finishing_times: finishing_time[cur_fin] = s
    return explored

def dfs_loop(G):
    global cur_leader
    explored = []
    nodes = list(G['nodes'].keys())
    # Loop
    for i in range(len(nodes)):
        v = nodes[i]
        if v not in explored:
            cur_leader = v
            explored = dfs(G, v, explored)

def dfs_loop_down(G):
    global cur_leader
    explored = []
    nodes = list(G['nodes'].keys())
    # Loop
    for i in range(len(nodes)-1,-1,-1):
        v = nodes[i]
        if v not in explored:
            cur_leader = v
            explored = dfs(G, v, explored)

def dfs_loop_f_times(G):
    # Reset data
    global cur_leader
    global record_finishing_times
    record_finishing_times = False
    global leaders
    leaders = {}
    explored = []
    # Loop backwards on finishing times data
    max_fin = cur_fin # Get final item entered in leaders
    for i in range(max_fin,-1,-1):
        v = finishing_time[i]
        if v not in explored:
            cur_leader = v
            explored = dfs(G, v, explored)

def topological(G):
    # Orders graph starting at sink node and working back to base
    global order_index
    global ordering
    order_index = len(G['nodes'])
    ordering = {}
    dfs_loop(G)
    return ordering

def compute_scc(G):
    # DFS Loop on reverse graph
    G = graphs.reverse_graph_in_place(G)
    dfs_loop_down(G)
    # DFS Loop on regular graph
    G = graphs.reverse_graph_in_place(G)
    dfs_loop_f_times(G)
    return leaders

if __name__ == "__main__":
    # Generate graph
    # G = graphs.get_connected_nodes()
    # # DFS basics
    # explored = dfs(G, 0)
    # print("Explored nodes in this order: {}".format(explored))
    # # Topological Ordering
    # G = graphs.get_directed_graph()
    # f = topological(G)
    # print("Graph ordering: {}".format(f))
    # Compute SCC
    G = graphs.get_scc_graph()
    l = compute_scc(G)
    print("Leaders/SCCs: {}".format(l))
