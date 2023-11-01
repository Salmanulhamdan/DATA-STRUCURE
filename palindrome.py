str=input("enter a string")
length=len(str)
for i in range(0,length):
    if str[i]==str[length-1-i]:
        flag=1
    else:
        flag=0
if flag==1:
    print("palindrome")
else:
    print("not a palindrome")
# def is_palindrome(x):
#     s = str(x)
#     return s == s[::-1]
# print(is_palindrome(-121))


# a="hello"
# print(a[::-1])