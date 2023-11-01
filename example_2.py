arr=[1,3,4,5,6,2,5]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[i]<=arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)
