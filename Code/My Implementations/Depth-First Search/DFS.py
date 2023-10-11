def depth_first_search(Adj, s, parent = None):
    # Implemented to solve single source reachability.
    if not parent: 
        parent = [None for _ in range(len(Adj))]
        parent[s] = s
    for u in Adj[s]:
        if not parent[u]:
            parent[u] = s
            depth_first_search(Adj, u, parent)
    order.append(s)        
    return parent


Adj = {
    0 : [1, 3, 5],
    1 : [2],
    2 : [3, 4],
    3 : [4],
    4 : [],
    5 : [4],
} 
order = []
parent = depth_first_search(Adj, 0)
print("Finishing order of DFS: ", order)
print("Topological sort, given a DAG fully accessable from the source: ", list(reversed(order)))
# The nodes with a parent can be explored.
print("Parents of each node: ", parent)
