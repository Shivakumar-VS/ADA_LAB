def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example
numbers = [64, 34, 25, 12, 22, 11, 90]

print("Before Sorting:", numbers)
bubble_sort(numbers)
print("After Sorting:", numbers)