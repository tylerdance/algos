""" 
Intersection of two arrays
Another classic!

Given two arrays of integers, return an array that contains just the elements that are present in both input arrays. The input arrays are not guaranteed to be sorted, but any given element will only appear once in a given input array.

Sample 1: intersection([0, 1, 4, 5, 8], [0, 2, 7, 9, 4]) -> [0, 4]
"""

""" jaxon's solution """
# def intersection(list1, list2):
#     solution_list = [i for i in list1 if i in list2]
#     return solution_list

""" bad quadratic nested for loop solution """
# def intersection(list1, list2):
#     list3 = []
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 list3.append(i)
#     return list3


""" pete's solution (linear time complexity) """
def intersection(list1, list2):
    dictionary = {}
    list3 = []

    for a in list1:
        dictionary[str(a)] = 'soucy'

    for b in list2:
        if str(b) in dictionary:
            list3.append(b)
    return list3

""" with set """
# def intersection(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)

#     return list(set1 & set2)

print(intersection([0, 1, 4, 5, 8], [0, 2, 7, 9, 4]))