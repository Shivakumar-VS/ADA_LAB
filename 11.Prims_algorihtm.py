import heapq
def prims_algorithm(graph):
  V = len(graph)
  mst = []
  visited = [False] * V
  pq = [(0, 0)]  # (weight, vertex)

  while pq:
    weight, u = heapq.heappop(pq)

    if visited[u]:
      continue
    visited[u] = True 
    mst.append((weight, u))

    for v , w in graph[u]:
      if not visited[v]:
        heapq.heappush(pq, (w,v))
  return mst
  
graph = {
  0:[(1, 2), (3, 6)],
  1:[(0, 2), (2, 3), (3, 8), (4, 5)],
  2:[(1, 3), (4, 7)],
  3:[(0, 6), (1, 8)],
  4:[(1, 5), (2, 7)]
}

mst = prims_algorithm(graph)
print("Edges in the Minimum Spanning Tree:")
for weight, vertex in mst:
  print(f"Vertex: {vertex}, Weight: {weight}")
