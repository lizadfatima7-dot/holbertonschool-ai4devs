## Bug 1 – bug1.py
**Intended Behavior**: Return a list containing only the last n elements.
**Issue Type**: Off-by-one error.
**Notes**: Loop uses len(items)+1. Change to len(items) to avoid IndexError.

## Bug 2 – bug2.py
**Intended Behavior**: Return the factorial of n (factorial(0) = 1).
**Issue Type**: Logical error.
**Notes**: Result starts at 0 and range excludes n. Set result=1 and use range(1, n+1).

## Bug 3 – bug3.js
**Intended Behavior**: Return the arithmetic mean of numbers, rounded to 2 decimal places.
**Issue Type**: Logic error.
**Notes**: NaN passes filter and reduce lacks initial value. Use Number.isNaN and initial value 0.

## Bug 4 – bug4.js
**Intended Behavior**: Fetch JSON and return user names in uppercase.
**Issue Type**: Async/Await error.
**Notes**: fetch and response.json return Promises. Add await before each call.

## Bug 5 – bug5.java
**Intended Behavior**: Return the most frequent word in a sentence.
**Issue Type**: Runtime exception.
**Notes**: Null input and missing keys in Map cause crashes. Add null guard and use getOrDefault.

## Bug 6 – bug6.py
**Intended Behavior**: Calculate averages from CSV and write to a new CSV.
**Issue Type**: Type mismatch.
**Notes**: CSV values are strings. Convert to float() and use with-blocks for file handling.