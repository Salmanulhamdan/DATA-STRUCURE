#bubblesort1
arr=[3.14, 2.71, 1.41, 1.73, 2.24, 1.62]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if (arr[j]> arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]

print (arr)
