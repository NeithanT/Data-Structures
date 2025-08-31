"""
    The use for two pointers is to maintain a pointer 
    for each end of a data structure (like an array or a list)
    and move them towards each other to find a solution.

    Key aspects:
    - Works mostly on sorted data structures
"""

def search_target(arr, target):

    """
        This function uses the two-pointer technique to find two numbers
        in a sorted array that add up to a target.
    """

    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer < right_pointer:
        current_sum = arr[left_pointer] + arr[right_pointer]
        if current_sum == target:
            return [left_pointer, right_pointer]
        elif current_sum < target:
            left_pointer += 1
        else:
            right_pointer -= 1

    return None


def binary_search(arr, target):

    """
        This function uses binary search, which
        follows the concept of divide and conquer
        or the two pointer technique.
    """

    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left_pointer = mid + 1
        else:
            right_pointer = mid - 1

    return None

# More Two-Pointer Examples

def remove_duplicates(arr):

    """
        Removes duplicates from a sorted array in-place.
        Returns the length of the array with unique elements.
    """

    if not arr:
        return 0

    left_pointer = 0
    for right_pointer in range(1, len(arr)):
        [1,2,2,2,4]
        if arr[right_pointer] != arr[left_pointer]:
            left_pointer += 1
            arr[left_pointer] = arr[right_pointer]

    return left_pointer + 1

def reverse_array(arr):
    """
        Reverses an array using two pointers.
        Without tuples, an extra variable is needed.
    """
    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer < right_pointer:
        arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
        left_pointer += 1
        right_pointer -= 1

def is_palindrome(string):
    """
        Checks if a string is a palindrome using two pointers.
    """
    left_pointer = 0
    right_pointer = len(string) - 1

    while left_pointer < right_pointer:
        if string[left_pointer] != string[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1

    return True

# TODO Add sorting, quick sort and merge sort, some more