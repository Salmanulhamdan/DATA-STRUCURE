def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[j] <arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


arr = [9,3,2,6,1,2,8]
print(selection_sort(arr))
