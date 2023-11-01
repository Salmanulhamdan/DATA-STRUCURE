def swap():
    if array[i]< array[j]:
        temp = array[i]
        array[i] = array[j]
        array[j] = temp


size = int(input("enter the size of array"))
a = 0
array = []
print("enter values")
for i in range(size):
    array.append(int(input()))
print(array)
for i in range(0, size+1):
    for j in range(i + 1, size):
        swap()
print(array)