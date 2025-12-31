edges = [(0,1,4),(0,2,4),(1,2,2),(1,0,4),(2,0,4),(2,1,2),(2,3,3),(2,5,2),(2,4,4),(3,4,3),(3,5,1),(4,5,3)]

parent = list(range(6))
def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]

mst = []

for u,v,w in sorted(edges, key = lambda x: x[2]):
    x,y = find(u), find(v)
    if x!= y:
        mst.append((u,v,w))
        parent[x] = y

for u , v, w in mst:
    print(f"{u}-{v} : {w}")

print("Total cost of MST", sum(w for _,_, w in mst))