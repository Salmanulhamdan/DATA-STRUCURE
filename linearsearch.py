arr = [('Alice', 25), ('Bob', 30), ('Charlie', 28), ('David', 32), ('Emily', 27)]
target = ('Charlie', 28)

for i in range(len(arr)):
    if arr[i] == target:
        print("Element found at index", i)
        break
