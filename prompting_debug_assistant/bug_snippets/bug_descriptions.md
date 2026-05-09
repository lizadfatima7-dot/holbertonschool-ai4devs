# Bug Descriptions

### Bug 1: bug1.py
- **Intended Behavior**: Return a new list containing only the last `n` elements.
- **Issue Type**: Off-by-one error.
- **Fix**: Replace `len(items)+1` with `len(items)` in the loop range to avoid `IndexError`.

### Bug 2: bug2.py
- **Intended Behavior**: Return the factorial of `n`. `factorial(0)` should return 1.
- **Issue Type**: Logical error.
- **Fix**: Initialize `result` to 1 and use `range(1, n + 1)` to include `n` in the product.

### Bug 3: bug3.js
- **Intended Behavior**: Filter non-numeric values and return the mean rounded to 2 decimal places.
- **Issue Type**: Off-by-one error / Logic error.
- **Fix**: Use `Number.isNaN` for filtering, provide an initial value of 0 to `reduce`, and use `parseFloat` on the `toFixed` result.

### Bug 4: bug4.js
- **Intended Behavior**: Fetch a JSON array of users and return names in uppercase.
- **Issue Type**: Misuse of data types (Async/Await).
- **Fix**: Add `await` keyword before `fetch()` and `response.json()` to handle promises correctly.

### Bug 5: bug5.java
- **Intended Behavior**: Count word frequencies and return the most frequent word.
- **Issue Type**: Runtime exception (NullPointer).
- **Fix**: Add a null guard for the input string and use `getOrDefault(word, 0) + 1` for the map updates.

### Bug 6: bug6.py
- **Intended Behavior**: Read scores from CSV, compute averages, and write to a new CSV.
- **Issue Type**: Misuse of data types / Resource leak.
- **Fix**: Convert string scores to `float()` and wrap file operations in `with open()` blocks.