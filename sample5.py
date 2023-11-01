# arr=[3,5,6,7,2,1]
# for i in range(1,len(arr)):
#     j=i
#     while j>=0 and arr[j]>arr[j-1]:
#         arr[j],arr[j-1]=arr[j-1],arr[j]
#         j-=1
# print(arr)
def removeDuplicates( nums) -> int:
    if len(nums) == 0:
        return 0

    i = 0
    for j in range(1, len(nums)):
          if nums[i] != nums[j]:
             i += 1
             nums[i] = nums[j]
    return i + 1
nums=[1,1,2,3,4,4,5,5,6,7,7]
print(removeDuplicates(nums))