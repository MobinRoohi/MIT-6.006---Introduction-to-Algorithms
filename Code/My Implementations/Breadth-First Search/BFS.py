def breadth_first_search(Adj, s):
    level = [[s]]
    parent = {v : None for v in Adj}
    parent[s] = s

    while len(level[-1]) > 0:
        level.append([])
        for u in level[-2]:
            for v in Adj[u]:
                if parent[v] == None:
                    level[-1].append(v)
                    parent[v] = u

    return parent, level

Adj = {
    0 : [1, 3, 5],
    1 : [2],
    2 : [3, 4],
    3 : [4],
    4 : [],
    5 : [4],
} 

parent, level = breadth_first_search(Adj, 0)
print(parent)
print(level)