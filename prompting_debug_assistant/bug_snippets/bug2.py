"""
Intended: Compute the factorial of a non-negative integer.
Bug Type: Logical error (wrong base case + wrong loop range)
"""

def factorial(n):
    if n == 1:          # BUG: base case misses n == 0 (0! = 1)
        return 1
    result = 0          # BUG: should be 1, using 0 makes every result 0
    for i in range(1, n):   # BUG: should be range(1, n+1), misses multiplying by n
        result *= i
    return result


print(factorial(5))   # Expected: 120, Got: 0
print(factorial(1))   # Expected: 1,   Got: 1
print(factorial(0))   # Expected: 1,   Crashes (RecursionError or wrong result)
