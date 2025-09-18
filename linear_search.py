# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def linear_search(list, target):
    # returns the index position of the target if found, else returns None
    for index in range(0, len(list)):
        if list[index] == target:
            return index
    return None

def verify_linear_search(index):
    if index is not None:
        print("Index found at index:", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 6)


if __name__ == '__main__':
    verify_linear_search(result)
