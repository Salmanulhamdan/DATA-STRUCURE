# def largestNumber(nums):
#     nums = [str(num) for num in nums]
#
#     def compare(a, b):
#         if a + b > b + a:
#             return -1
#         elif a + b < b + a:
#             return 1
#         else:
#             return 0
#
#     nums.sort(key=compare)
#
#     result = ''.join(nums)
#     result = result.lstrip('0')
#
#     if result == '':
#         return '0'
#     else:
#         return result

# def largest_number(nums):
    # # Convert the list of integers to a list of strings
    # nums = [str(x) for x in nums]
    #
    # # Define the comparison function
    # def compare(x, y):
    #     return int(y + x) - int(x + y)
    #
    # # Sort the list of strings using the comparison function
    # nums.sort(key=(compare()))
    #
    # # Join the sorted strings together to form the result
    # result = ''.join(nums)
    #
    # # Remove leading zeros from the result
    # result = result.lstrip('0')
    #
    # # Handle the case where the result is an empty string (i.e., all inputs were 0)
    # if not result:
    #     result = '0'
    #
    # return result

# Example usage:
nums = [3,30,34,5,9]
# print(largest_number(nums))
# Output: "9534330"

nums = [str(num) for num in nums]
nums.sort(reverse=True)

nums=''.join(nums)
nums = nums.lstrip('0')
print(nums)