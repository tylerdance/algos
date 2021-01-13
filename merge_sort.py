""" pete's version """
def merge(arr1, arr2):
    output = []
    start_length_arr1 = len(arr1)
    start_length_arr2 = len(arr2)
    target_output_length = start_length_arr1 + start_length_arr2

    # OR:
    # while len(arr1) > 0 or len(arr2) > 0
    while len(output) < target_output_length:
        print('-----')
        print('arr1', arr1)
        print('arr2', arr2)
        print('output', output)

        if len(arr1) == 0:
            output += arr2
            arr2 = []
        elif len(arr2) == 0:
            output += arr1
            arr1 = []
        elif arr1[0] < arr2[0]:
            output.append(arr1[0])
            arr1 = arr1[1:]
        else:
            output.append(arr2[0])
            arr2 = arr2[1:]

    return output

# helper split function
def split(arr):
    print('splitting: ', arr)
    midpoint = len(arr) // 2
    arr1 = arr[:midpoint]
    arr2 = arr[midpoint:]
    
    if len(arr1) <= 1 and len(arr2) <= 1:
        # fire base case
        return merge(arr1, arr2)
    
    split_arr1 = split(arr1)  
    split_arr2 = split(arr2)
    return merge(split_arr1, split_arr2)

print(split([4,5,7,8,2,1]))



# print(merge([2], [4]))
# print(merge([1, 3], [2, 4]))


# def merge(a, b):
#     merged_list = []
#     i = 0
#     j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             merged_list.append(a[i])
#             i += 1
#         else:
#             # append whichever is smaller on to merged_list
#             merged_list(b[j])
#             j += 1
#     if len(a) > i:
#         merged_list = merged_list + a
#     elif len(b) > j:
#         merged_list = merged_list + b
#     return merged_list

# def merge_sort(n):
#     if len(n) <= 1:
#         return n
    
#     split_point = int(len(n) / 2)
#     left = merge_sort(n[:split_point])
#     right = merge_sort(n[split_point:])

#     return merge(left, right)

# print(merge_sort([2,6,9,3,5,7,2,7,0,2]))