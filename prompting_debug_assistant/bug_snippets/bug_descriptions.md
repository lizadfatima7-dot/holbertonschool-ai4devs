## Bug 1 – bug1.py

**Intended Behavior**: Return the last n items of a list. For example, `get_last_n([10, 20, 30, 40, 50], 3)` should return `[30, 40, 50]`.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses `range(start, len(items) + 1)` instead of `range(start, len(items))`, causing it to iterate one index past the last valid position. This raises an `IndexError` when `n` equals the length of the list, crashing the function instead of returning the expected result.

## Bug 2 – bug2.py

**Intended Behavior**: Compute and return the factorial of a non-negative integer. For example, `factorial(5)` should return `120` and `factorial(0)` should return `1`.
**Issue Type**: Logical error.
**Notes**: The base case only handles `n == 1`, missing `n == 0`. The result is initialized to `0` instead of `1`, so all multiplications produce `0`. The loop range excludes `n` itself, meaning the function always returns `0` instead of the correct factorial value.

## Bug 3 – bug3.js

**Intended Behavior**: Filter non-numeric values from an array and return the numeric average of the remaining values rounded to 2 decimal places. For example, `average([10, "hello", null, 20])` should return `15.00`.
**Issue Type**: Data type misuse and runtime exception.
**Notes**: `typeof NaN === "number"` allows `NaN` to pass the filter, corrupting the sum. The `reduce` call has no initial value, causing a `TypeError` on empty arrays instead of a safe fallback. The `toFixed` method returns a string, not a number, breaking any downstream arithmetic that expects a numeric result.

## Bug 4 – bug4.js

**Intended Behavior**: Fetch a list of users from an API endpoint and return their names in uppercase. For example, the function should return `["LEANNE GRAHAM", "ERVIN HOWELL", ...]` for a valid URL.
**Issue Type**: Misuse of async/await.
**Notes**: The `fetch` call is missing `await`, so `response` holds a `Promise` instead of the actual HTTP response. Calling `.json()` on a `Promise` throws a `TypeError`, crashing the function before any data is processed. The result is never awaited at the call site, so the caller receives a pending `Promise` instead of the expected array of names.

## Bug 5 – bug5.java

**Intended Behavior**: Count the frequency of each word in a sentence and return the most frequently occurring word. For example, given `"the cat sat on the mat the cat"`, the function should return `"the"`.
**Issue Type**: Runtime NullPointerException and logical error.
**Notes**: No null check exists for the input sentence, so passing `null` throws a `NullPointerException` on `.toLowerCase()`. `HashMap.get()` returns `null` for unseen words, and adding `1` to `null` throws a `NullPointerException`, preventing the word count from being built. The `>=` operator in `mostFrequent` makes tie-breaking non-deterministic, so the returned word may vary between runs when multiple words share the highest frequency.

## Bug 6 – bug6.py

**Intended Behavior**: Read a CSV file of student names and scores, compute each student's average score, and write the results to a new CSV file with columns `Name` and `Average`.
**Issue Type**: Runtime TypeError and resource leak.
**Notes**: CSV values are read as strings, so passing them to `sum()` raises a `TypeError` and halts execution before any output is produced. Files are opened without `with` statements, so neither file is properly closed if an exception occurs. The output file is never explicitly closed on success, risking incomplete or corrupted data being written to disk.