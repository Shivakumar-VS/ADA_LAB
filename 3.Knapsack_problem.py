class Item:
  def __init__(self, value, weight):
    self.value = value
    self.weight = weight 

def fractional_knapsack(items, capacity):
    items.sort(key = lambda x : x.value / x.weight, reverse = True)
    total_value = 0.0
    for item in items:
      if capacity >= item.weight:
        capacity -= item.weight
        total_value += item.value
      else:
        total_value += item.value * (capacity / item.weight)
        break
    return total_value

items = [Item(60,100), Item(100,20), Item(120, 30)]
capacity = 50
max_value = fractional_knapsack(items, capacity)
print(f"Maximum value in the Knapsack = {max_value}")