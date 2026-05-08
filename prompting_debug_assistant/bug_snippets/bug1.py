"""
Intended: Return the last n items from a list.
Bug Type: Off-by-one error
"""

def get_last_n(items, n):
    result = []
    start = len(items) - n  # BUG: should be len(items) - n, but the loop below uses wrong range
    for i in range(start, len(items) + 1):  # BUG: +1 causes IndexError on last iteration
        result.append(items[i])
    return result


# Test
my_list = [10, 20, 30, 40, 50]
print(get_last_n(my_list, 3))   # Expected: [30, 40, 50]
print(get_last_n(my_list, 5))   # Expected: [10, 20, 30, 40, 50] — crashes here
