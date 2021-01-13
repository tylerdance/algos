""" pete's version """
# find mid index
# base case: if you get very lucky and the value is the target value return the mid index
    # OR if the length of array is 1 and the element isn't the value, return -1
    # OR if the length of the array is 0, return -1
# split the array into left and right halves
# recur on whichever half of the array might contain the target value

def search(arr, target, lost_index = 0):
  if len(arr) == 0:
    return -1
  mid_index = len(arr) // 2
  mid_value = arr[mid_index]
  left_half = arr[:mid_index]
  right_half = arr[mid_index + 1:]
  # print(mid_value)
  # print(left_half)
  # print(right_half)
  if mid_value == target:
    return mid_index + lost_index
  elif len(arr) == 1 and mid_value != target:
    return -1
  elif mid_value < target:
    return search(right_half, target, mid_index + 1 + lost_index)
  elif mid_value > target:
    return search(left_half, target, lost_index)
# print(search([1,2,3,4,5,6,7,8,9], 5))
# print(search([1,2,3,4,5,6,7,8,9], 3.5))
print(search([1,2,3,4,5], 4))


# def binary_search(arr, x):
#     print('splitting: ', arr)

#     midpoint = 0
#     first = 0
#     last = len(arr) - 1
#     while first <= last:
#         midpoint = (first + last) // 2
#         if x < arr[midpoint]:
#             last = midpoint - 1
#         elif x > arr[midpoint]:
#             first = midpoint + 1
#         else:
#             return midpoint
