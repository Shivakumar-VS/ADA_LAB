# python program to implement selection sort

def selection_sort(arr, n):
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i+1, n):
      if (arr[j] < arr[min_idx]):
        min_idx = j
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
  arr.append(int(input("Enter element: ")))
print("Unsorted array:", arr)
sorted_arr = selection_sort(arr, n)
print("Sorted array:", sorted_arr)
