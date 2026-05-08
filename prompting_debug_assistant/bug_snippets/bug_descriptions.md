````md
# Bug Analysis Report

## Bug 1 - bug1.py

### Intended Behavior
Return the last `n` items of a list.

Example:

```python
get_last_n([10, 20, 30, 40, 50], 3)
```

Expected output:

```python
[30, 40, 50]
```

### Issue Type
Off-by-one error

### Notes
The loop uses:

```python
range(start, len(items) + 1)
```

instead of:

```python
range(start, len(items))
```

This causes the loop to iterate one index beyond the valid range of the list.

When `i == len(items)`, the code attempts to access an invalid index, raising an `IndexError`.

---

## Bug 2 - bug2.py

### Intended Behavior
Compute and return the factorial of a non-negative integer.

Examples:

```python
factorial(5) -> 120
factorial(0) -> 1
```

### Issue Type
Logical error

### Notes
The base case only handles `n == 1`, missing the valid case `n == 0`.

The variable `result` is initialized to `0` instead of `1`, so every multiplication keeps the value at `0`.

The loop uses:

```python
range(1, n)
```

which excludes `n` itself from the multiplication.

Because of these issues, the function always returns `0` instead of the correct factorial value.

---

## Bug 3 - bug3.js

### Intended Behavior
Filter non-numeric values from an array and return the numeric average of the remaining values rounded to 2 decimal places.

Example:

```javascript
average([10, "hello", null, 20])
```

Expected output:

```javascript
15.00
```

### Issue Type
Data type misuse and runtime exception

### Notes
The filter only checks:

```javascript
typeof n === "number"
```

which still allows `NaN` because `typeof NaN === "number"` evaluates to `true`.

The `reduce()` call does not provide an initial value, so calling it on an empty array throws a `TypeError`.

Additionally, `toFixed(2)` returns a string rather than a number, which may cause problems in later arithmetic operations.

---

## Bug 4 - bug4.js

### Intended Behavior
Fetch a list of users from an API endpoint and return their names in uppercase.

Example output:

```javascript
["LEANNE GRAHAM", "ERVIN HOWELL"]
```

### Issue Type
Misuse of async/await

### Notes
The `fetch()` call is missing `await`, so `response` becomes a `Promise` instead of the resolved HTTP response object.

Incorrect code:

```javascript
const response = fetch(url);
```

Correct code:

```javascript
const response = await fetch(url);
```

The `.json()` call also requires `await`.

Without awaiting these operations, the code attempts to call `.map()` on unresolved Promise data, causing runtime errors.

The returned result is also not awaited at the call site, so the console prints a pending `Promise` instead of the final array of names.

---

## Bug 5 - bug5.java

### Intended Behavior
Count the frequency of each word in a sentence and return the most frequently occurring word.

Example:

```java
"the cat sat on the mat the cat"
```

Expected output:

```java
"the"
```

### Issue Type
Runtime NullPointerException and logical error

### Notes
The function does not check whether the input sentence is `null`.

Calling:

```java
sentence.toLowerCase()
```

when `sentence` is `null` throws a `NullPointerException`.

Additionally, `counts.get(word)` returns `null` for words that do not yet exist in the map.

This line:

```java
counts.get(word) + 1
```

attempts arithmetic with `null`, causing another `NullPointerException`.

The comparison:

```java
>=
```

inside `mostFrequent()` also creates inconsistent tie-breaking behavior because later words replace earlier ones when frequencies are equal.

---

## Bug 6 - bug6.py

### Intended Behavior
Read a CSV file of student names and scores, compute each student's average score, and write the results to a new CSV file.

Expected output columns:

```python
["Name", "Average"]
```

### Issue Type
Runtime TypeError and resource leak

### Notes
CSV values are read as strings, but `sum()` requires numeric values.

This causes a `TypeError` during average calculation.

The scores should be converted using `int()` or `float()` before summation.

The files are opened without `with` statements:

```python
open(input_path, "r")
```

and

```python
open(output_path, "w")
```

If an exception occurs, the files may remain open.

The output file is also never explicitly closed, which can result in incomplete or corrupted output data.
````
