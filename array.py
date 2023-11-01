size=int(input("enter the size of array"))
array1=[]
print("enter the values")
i=0
while i<=size:
    array1.append(int(input()))
    i+=1
print("array1",array1)
array2=array1.copy()
array2.append(int(input("add element to the seccond array")))
array2.insert(int(input("enter position to add seccond value")),int(input("enter the value")))
print(array1)
print(array2)