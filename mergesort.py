def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return sorting(merge_sort(left_half), merge_sort(right_half))
def sorting(le, re):
    sorted_arr = []
    i = j = 0
    while i < len(le) and j < len(re):
        if le[i] <= re[j]:
            sorted_arr.append(le[i])
            i += 1
        else:
            sorted_arr.append(re[j])
            j += 1
    sorted_arr +=le[i:]
    sorted_arr +=re[j:]
    return sorted_arr
unsorted_arr = [10.6,7.8, 8,-9,7.5,-9.4,6]
print(unsorted_arr)
sorted_arr = merge_sort(unsorted_arr)
print(sorted_arr)
