"""
    The use for two pointers is to maintain a pointer 
    for each end of a data structure (like an array or a list)
    and move them towards each other to find a solution.

    Key aspects:
    - Works mostly on sorted data structures
"""
# Same Direction

def remove_duplicates(arr):

    """
        Removes duplicates from a sorted array in-place.
        Returns the length of the array with unique elements.
    """

    if not arr:
        return 0

    left_pointer = 0
    for right_pointer in range(1, len(arr)):
        
        if arr[right_pointer] != arr[left_pointer]:
            left_pointer += 1
            arr[left_pointer] = arr[right_pointer]

    return left_pointer + 1

# Fast/Slow Pointer

# Sliding Window

def longest_substring(string):
    """
        Finds the length of the longest substring without repeating characters.
    """

    left_pointer = 0
    max_length = 0
    char_map = {}

    for ch_index in range(0,len(string)):
        continue

    return max_length
    

# Pointers In Opposite Direction

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
        The binary search algorithm, 
        where the array is divided in the middle
        to find the wanted element.

        This can also be applied to monotonic functions
        or structures, monotonic means it has a constant
        growth
        
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

def find_minimum_rotated_arr(arr):
    """
        Leetcode 153

        Given a sorted rotated array
    """
    
    left_pointer = 0
    right_pointer = len(arr) -1

    while left_pointer < right_pointer:
        continue

    return right_pointer - left_pointer

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