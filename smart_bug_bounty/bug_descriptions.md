# Bug Descriptions

## Bug 1 – bug1.py
- **Intended Behavior**: Return a new list containing only the last n elements.
- **Issue Type**: Off-by-one error.
- **Notes**: Loop uses `len(items)+1` as upper bound, causing `IndexError`. Replace with `len(items)`.

## Bug 2 – bug2.py
- **Intended Behavior**: Return the factorial of n, ensuring `factorial(0)` returns 1.
- **Issue Type**: Logical error.
- **Notes**: `result` initialized to 0 makes all products zero. Set `result=1` and use `range(1, n+1)`.

## Bug 3 – bug3.js
- **Intended Behavior**: Filter non-numeric values and return mean rounded to 2 decimal places.
- **Issue Type**: Logic error.
- **Notes**: `NaN` passes `typeof` check. Use `Number.isNaN` and provide an initial value of 0 to `reduce`.

## Bug 4 – bug4.js
- **Intended Behavior**: Fetch a JSON array of users and return names in uppercase.
- **Issue Type**: Misuse of asynchronous libraries.
- **Notes**: `fetch` and `json()` return Promises but are not awaited. Add `await` before each call.

## Bug 5 – bug5.java
- **Intended Behavior**: Count word frequencies and return the most frequent word.
- **Issue Type**: Runtime Exception (NullPointer).
- **Notes**: Null inputs and missing keys in the map cause crashes. Add null guards and use `getOrDefault`.

## Bug 6 – bug6.py
- **Intended Behavior**: Read scores from CSV, compute student averages, and write to a new CSV.
- **Issue Type**: Type mismatch and resource management.
- **Notes**: CSV values are strings. Convert to `float()` and use `with open()` blocks for file handling.