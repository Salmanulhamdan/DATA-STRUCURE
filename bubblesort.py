#bubblesort1
print("\r")
arr=[3.14, 2.71, 1.41, 1.73, 2.24, 1.62]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if (arr[j]> arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]

print (arr)

print("\r")
for j in range(10):
    print ('*'*j)
print("\r")
print("\r")


for i in range(0,10):
    for j in range(0,i+1):
          print("* ",end="")
    print("\r")
    
