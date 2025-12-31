from itertools import permutations

def calculate_distance(route, distance_matrix):
  return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1)) + distance_matrix[route[-1]][route[0]]

def travelling_salesman(distance_matrix):
  cities = list(range(len(distance_matrix)))
  shortest_route = None
  min_distance = float('inf')

  for route in permutations(cities):
    current_distance = calculate_distance(route, distance_matrix)
    if current_distance < min_distance:
      min_distance = current_distance
      shortest_route = route
    return shortest_route, min_distance
  
# Example usage
distance_matrix = [
  [0, 10, 15, 20],
  [10, 0, 35, 25],
  [15, 35, 0, 30],
  [20, 25, 30, 0]
]

shortest_route, min_distance = travelling_salesman(distance_matrix)
print("Shortest route:", shortest_route)
print("Minimum distance:", min_distance)