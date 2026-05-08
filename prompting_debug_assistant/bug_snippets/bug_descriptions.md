# Bug Report

---

## Bug 1 – bug1.py

### Intended Behavior
Return the last n items of a list as a new list. For example, `get_last_n([10, 20, 30, 40, 50], 3)` should return `[30, 40, 50]`.

### Issue Type
Off-by-one error.

### How It Deviates
The loop uses `range(start, len(items) + 1)` instead of `range(start, len(items))`, causing it to iterate one index past the end of the list. Instead of returning the correct slice, the function raises an `IndexError` and crashes entirely when `n` equals the length of the list.

### Real-World Impact
Any application relying on this function to paginate or retrieve recent records (e.g., showing the last 5 transactions) would crash rather than returning the expected data, breaking the feature completely for the user.

---

## Bug 2 – bug2.py

### Intended Behavior
Compute and return the factorial of a non-negative integer. For example, `factorial(5)` should return `120` and `factorial(0)` should return `1`.

### Issue Type
Logical error.

### How It Deviates
Three compounding mistakes prevent the function from ever returning a correct result: the base case misses `n == 0`, `result` is initialized to `0` instead of `1` (making all multiplications produce `0`), and the loop range excludes `n` itself. Instead of computing the factorial, the function always returns `0` for any input greater than `1` and raises no error for `n == 0`.

### Real-World Impact
In mathematical or scientific applications (e.g., computing probabilities or permutations), silently returning `0` instead of the correct factorial would produce completely wrong results without any error or warning, making the bug very difficult to detect.

---

## Bug 3 – bug3.js

### Intended Behavior
Filter out non-numeric values from an array and return the numeric average of the remaining values, rounded to 2 decimal places. For example, `average([10, "hello", null, 20])` should return `15.00`.

### Issue Type
Data type misuse and runtime exception.

### How It Deviates
`typeof NaN === "number"` evaluates to `true`, so `NaN` passes the filter and corrupts the sum. The `reduce` call has no initial value, throwing a `TypeError` on empty arrays instead of returning a safe fallback. Additionally, `toFixed(2)` returns a string, not a number, so callers expecting a numeric result receive the wrong type.

### Real-World Impact
A data dashboard computing averages from user input would silently produce `NaN` when invalid values are present, crash entirely on empty datasets, and cause downstream arithmetic to break due to the unexpected string return type.

---

## Bug 4 – bug4.js

### Intended Behavior
Fetch a list of users from an API endpoint and return their names converted to uppercase. For example, calling the function with a valid URL should return `["LEANNE GRAHAM", "ERVIN HOWELL", ...]`.

### Issue Type
Misuse of async/await.

### How It Deviates
The `fetch` call is missing `await`, so `response` holds an unresolved `Promise` instead of the actual HTTP response. Calling `.json()` on a `Promise` throws a `TypeError`, crashing the function before any data is accessed. At the call site, the result is also not awaited, so the caller receives a pending `Promise` object instead of the expected array of names.

### Real-World Impact
A user-facing feature that displays a list of names (e.g., a team directory or leaderboard) would show nothing and log an unhandled error in production, causing a broken UI with no meaningful feedback to the user.

---

## Bug 5 – bug5.java

### Intended Behavior
Count the frequency of each word in a sentence and return the most frequently occurring word. For example, given `"the cat sat on the mat the cat"`, the function should return `"the"`.

### Issue Type
Runtime NullPointerException and logical error.

### How It Deviates
Three distinct issues exist. First, no null check exists for the input sentence, so passing `null` causes a `NullPointerException` on `.toLowerCase()` before any processing begins. Second, `HashMap.get()` returns `null` for words not yet in the map, and adding `1` to `null` throws a `NullPointerException`, preventing the word count map from being built at all. Third, the `>=` operator in `mostFrequent` causes non-deterministic tie-breaking, so the returned word can differ across runs when multiple words share the highest frequency.

### Real-World Impact
A text analytics tool or search engine using this function would crash on any unseen word or null input, making it completely unusable in production. Even when it does not crash, inconsistent tie-breaking produces unreliable results that undermine the accuracy of the feature.

---

## Bug 6 – bug6.py

### Intended Behavior
Read a CSV file of student names and scores, compute each student's average score, and write the results to a new output CSV file with columns `Name` and `Average`.

### Issue Type
Runtime TypeError and resource leak.

### How It Deviates
CSV values are read as strings, so passing them directly to `sum()` raises a `TypeError` and halts execution before any averages are computed or written. Files are opened without `with` statements, so if the exception occurs mid-execution, neither the input nor the output file is properly closed. The output file is also never explicitly closed on success, risking incomplete or corrupted data on disk.

### Real-World Impact
A grading system or reporting tool using this function would crash on every run without producing any output file, leaving teachers or administrators with no results. Unclosed file handles may also lock the files on certain operating systems, preventing other processes from accessing them.