# Implement function to print in-degree and out-degree to display that adjacency matrix representation of directed graph

class Graph:
  def __init__(self, size):
    self.size = size
    self.adj_matrix = [[0] * size for _ in range(size)]

  def add_edge(self, src, dest):
      self.adj_matrix[src][dest] = 1

  def in_degree(self, vertex):
      return sum(row[vertex] for row in self.adj_matrix)

  def out_degree(self, vertex):
      return sum(self.adj_matrix[vertex])
    
  def print_matrix(self):
      for row in self.adj_matrix:
        print(''.join(map(str, row)))

  def print_degrees(self):
      for i in range(self.size):
        print(f"Vertex {i}: In-Degree = {self.in_degree(i)}, Out-Degree = {self.out_degree(i)}")

g = Graph(4)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)

print("Adjacency Matrix:")
g.print_matrix()
print("\nIn-Degree and Out-Degree of each vertex:")
g.print_degrees()