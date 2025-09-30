def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint= (len(list))//2
        if list[midpoint] == target:
            return True
        if list[midpoint] < target:
            return recursive_binary_search(list[midpoint+1:], target)
        else:
            return recursive_binary_search(list[:midpoint], target)

def verify_binary_search(result):
    print("Verifying Binary Search", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = recursive_binary_search(numbers, 12)
verify_binary_search(result)

result = recursive_binary_search(numbers, 6)
verify_binary_search(result)