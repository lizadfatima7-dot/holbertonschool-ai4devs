# Bug Descriptions

## bug1.py
- **Intended Behavior**: Return a new list containing the last `n` elements.
- **Issue Type**: Off-by-one error.
- **Notes**: Loop uses `len(items)+1` causing IndexError. Fix by using `len(items)`.

## bug2.py
- **Intended Behavior**: Return the factorial of `n`. `factorial(0)` must return 1.
- **Issue Type**: Logical error.
- **Notes**: Result initialized to 0; range excludes `n`. Set `result=1` and use `range(1, n+1)`.

## bug3.js
- **Intended Behavior**: Return the arithmetic mean of numbers rounded to 2 decimal places.
- **Issue Type**: Logic error.
- **Notes**: `NaN` passes filter and `reduce` lacks initial value. Use `Number.isNaN` and initial value 0.

## bug4.js
- **Intended Behavior**: Fetch user objects and return names in uppercase.
- **Issue Type**: Misuse of libraries (Async/Await).
- **Notes**: `fetch` and `json()` are not awaited. Add `await` before both calls to handle Promises.

## bug5.java
- **Intended Behavior**: Return the most frequent word in a sentence.
- **Issue Type**: Runtime exception (NullPointer).
- **Notes**: Null inputs and missing map keys cause crashes. Add null guards and use `getOrDefault`.

## bug6.py
- **Intended Behavior**: Compute CSV averages and write to a new CSV file.
- **Issue Type**: Type mismatch / Resource leak.
- **Notes**: CSV values are strings. Convert to `float()` and use `with open()` blocks.