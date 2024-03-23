a=[-1,-10,-3]
length=len(a)
largest=float('-inf')
seccond=float('-inf')
for i in range(length):
    if a[i]>largest:
        seccond=largest
        largest=a[i]
    
            

print(seccond)




a=[1,2,3,4,5,6]
b=""
length=len(a)
# print(a[-1])
for i in range(length-1,-1,-1):

    print(a[i])


ch=[]
def reversestring(string):
    
    length=len(string)
    
    if length==0:
        return print(ch)
    ch.append(string[length-1])
    string.pop()
    return reversestring(string)
    
    

c=reversestring(a)
print(c)

def reverse(s):
    str = ""
    for i in s:
        print(i)
        str = i + str
    return str

def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]
 
s = "Geeksforgeeks"

ah=rreverse(s)
print(ah)

    

class Solution:
    def numIdenticalPairs(self, nums) :
        # set1={}
        count=0
        lenfth=len(nums)
        for i in range(lenfth):
            for j in range(i+1,lenfth):
                if nums[i]== nums[j]:
                    print("i:",nums[i],"j:",nums[j])
                    count+=1
                    
        return print(count)
    
nums=[1,2,3,1,1,4,3]   
obj=Solution()

obj.numIdenticalPairs(nums)