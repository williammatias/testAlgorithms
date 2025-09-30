def binary_search(list, target):
    # both of this run in constant time
    first = 0
    last = len(list) - 1
    # while loop is where the real cost is
    while first <= last:
        mid = (first + last) // 2 # floor division operator to round value
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None

def verify_binary_search(index):
    if index is not None:
        print("Index found at index:", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = binary_search(numbers, 12)

verify_binary_search(result)
