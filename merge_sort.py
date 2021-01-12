def merge(a, b):
    merged_list = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged_list.append(a[i])
            i += 1
        else:
            # append whichever is smaller on to merged_list
            merged_list(b[j])
            j += 1
    if len(a) > i:
        merged_list = merged_list + a
    elif len(b) > j:
        merged_list = merged_list + b
    return merged_list

def merge_sort(n):
    if len(n) <= 1:
        return n
    
    split_point = int(len(n) / 2)
    left = merge_sort(n[:split_point])
    right = merge_sort(n[split_point:])

    return merge(left, right)

print(merge_sort([2,6,9,3,5,7,2,7,0,2]))