def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    idx = 0

    while arrA != [] and arrB != []:
        if arrA[0] < arrB[0]:
            merged_arr[idx] = arrA[0]
            del arrA[0]
            idx += 1
        else:
            merged_arr[idx] = arrB[0]
            del arrB[0]
            idx += 1
    if arrA == []:
        merged_arr = merged_arr[:idx] + arrB
    else:
        merged_arr = merged_arr[:idx] + arrA

    return merged_arr


def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr
    mid = (len(arr) - 1) // 2

    left_array = merge_sort(arr[:mid+1])
    right_array = merge_sort(arr[mid+1:])

    arr = merge(left_array, right_array)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
    pass
