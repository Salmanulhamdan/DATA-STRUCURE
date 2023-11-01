def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j >= 0 and arr[j] > arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


arr2 = [3.14, 2.71, 1.41, 1.618, 0.577, 0.707]
insertion_sort(arr2)
print(arr2)
