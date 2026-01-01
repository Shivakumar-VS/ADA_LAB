# Write a program to find minimum and maximum value in an array using divide and conquer


def find_min_max(arr, low, high):
  #if the array contain only one element
  if low == high:
    return arr[low], arr[low]
  
  #if the array contains only two elements
  if high == low + 1:
    if arr[low] < arr[high]:
      return arr[low], arr[high]
    else:
      return arr[high], arr[low]
    
  #find the middle element
  mid = (low + high) // 2
  left_min, left_max = find_min_max(arr, low , mid)
  right_min, right_max = find_min_max(arr, mid+1, high)

  return min(left_min, right_min) , max(left_max, right_max)

arr = [3,5,1,8,2,9,6,4]
min_val , max_val = find_min_max(arr, 0 , len(arr) - 1)
print(f"The minimum value is {min_val}")
print(f"The maximum value is {max_val}")