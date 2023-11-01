# bubble sort
arr = [4, 3, 5, 2, 6, 8, 1, 7]
# for i in range(len(arr)):
#     for j in range(len(arr)-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
# print(arr)

for i in range(1, len(arr)):
    j = i
    while j > 0 and arr[j] > arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1
print(arr)
