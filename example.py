# array = [2,4,5,7,3,1]
# a = filter(lambda x: x % 2 == 0, array)
# b = list(map(lambda x: x ** 2, a))
# print(b)
# print(sorted(array))


def decr(func):
    def inner():
        a=func()

        return a.upper()
    return inner

@decr
def fun():

    return "hai"


print(fun())
# def count_down(n):
#     if n > 0:
#         yield n
#         yield from count_down(n - 1)
#
# # Usage
# for num in count_down(5):
#     print(num)
#
# def number_generator(n):
#     for i in range(1, n+1):
#         yield i
#
# # Usage
# for num in number_generator(5):
#     print(num)

#
# def binarysearch(arr,key):
#     l=0
#     r=len(arr)-1
#     while l<=r:
#         mid=(l+r)//2
#         if arr[mid]==key:
#             return mid
#         elif arr[mid]<key:
#             l=mid+1
#         else:
#             r=mid-1
#     return 0
# arr=[1,2,3,4,5,6,7]
# result=binarysearch(arr,4)
# if result != 0:
#     print("Element found at index", result)
# else:
#     print("Element not found in array")



