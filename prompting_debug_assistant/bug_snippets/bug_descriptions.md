# Bug Analysis Report

## Bug 1 - bug1.py

### Intended Behavior

Return the last `n` elements of a list in correct order without errors.

Example:

```python
get_last_n([10, 20, 30, 40, 50], 3)
```

Expected output:

```python
[30, 40, 50]
```

Edge case:
If `n == len(list)`, the function should return the entire list without crashing.

### Issue Type

Off-by-one error

### Notes

The loop incorrectly uses:

```python
range(start, len(items) + 1)
```

This goes beyond valid indices and causes `IndexError`.

Correct approach:

```python
range(start, len(items))
```

---

## Bug 2 - bug2.py

### Intended Behavior

Compute factorial of a non-negative integer correctly.

Examples:

```python
factorial(5) -> 120
factorial(0) -> 1
```

Edge case:
Factorial of 0 must return 1.

### Issue Type

Logical error

### Notes

`result` is initialized to `0`, which breaks multiplication logic.

The loop:

```python
range(1, n)
```

does not include `n`, so final multiplication step is missing.

Also base case only handles `n == 1`, missing `n == 0`.

---

## Bug 3 - bug3.js

### Intended Behavior

Filter only numeric values, compute average, and return result rounded to 2 decimal places.

Example:

```javascript
average([10, "hello", null, 20])
```

Expected output:

```
15.00
```

Edge case:
Empty arrays should not crash and should return a safe value (e.g., 0 or handled error).

### Issue Type

Data validation and runtime error

### Notes

`typeof NaN === "number"` allows invalid values into calculation.

`reduce()` without initial value causes crash on empty arrays.

`toFixed(2)` returns string instead of number.

---

## Bug 4 - bug4.js

### Intended Behavior

Fetch users from API and return uppercase names as an array.

Example:

```
["LEANNE GRAHAM", "ERVIN HOWELL"]
```

Edge case:
Function must wait for API response before processing data.

### Issue Type

Async/await misuse

### Notes

Missing `await` in `fetch()`:

```javascript
const response = fetch(url);
```

Also missing `await` for:

```javascript
response.json()
```

This leads to processing unresolved Promise objects instead of actual data.

---

## Bug 5 - bug5.java

### Intended Behavior

Count word frequency and return the most frequent word.

Example:

```
"the cat sat on the mat the cat" -> "the"
```

Edge case:
Function must handle `null` input safely.

### Issue Type

NullPointerException and logic error

### Notes

No null check before:

```java
sentence.toLowerCase()
```

This causes crash if input is null.

`counts.get(word) + 1` fails for new words (returns null).

Tie-breaking logic using `>=` causes inconsistent results.

---

## Bug 6 - bug6.py

### Intended Behavior

Read CSV file, compute student averages, and write results to output file.

Expected output:

```
Name, Average
```

Edge case:
File operations must safely close even if error occurs.

### Issue Type

Type conversion error and resource management issue

### Notes

CSV values are strings but used in `sum()` → causes `TypeError`.

Values must be converted using `int()` or `float()`.

Missing `with open()` causes file leak risk.

Output file is not safely closed if error occurs.
