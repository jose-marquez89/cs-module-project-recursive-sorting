# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    # base case
    if start > end or len(arr) < 1:
        return -1

    mid = (start + end) // 2
    if arr[mid] > target:
        end = mid - 1
    elif arr[mid] < target:
        start = mid + 1
    else:
        return mid

    return binary_search(arr, target, start, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
