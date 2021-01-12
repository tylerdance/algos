def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bubble_sort(arr):
    while not is_sorted(arr):
        for i in range(len(arr) - 1):
            # print(i)
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# print(is_sorted([1, 3, 10, 2]))
# print(is_sorted([1, 3, 10, 11]))

print(bubble_sort([19, 3, 10, 2]))