def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  mid = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  return quick_sort(left) + mid + quick_sort(right)

test_arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", test_arr)
sorted_arr = quick_sort(test_arr)
print("Sorted array:", sorted_arr)