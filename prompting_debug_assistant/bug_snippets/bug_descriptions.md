# Bug Analysis Report

## Bug 1 - bug1.py

### Intended Behavior

The function should return the last `n` elements of a list.

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

This causes the function to access one index beyond the valid range, producing an `IndexError`.

---

## Bug 2 - bug2.py

### Intended Behavior

The function should compute the factorial of a non-negative integer.

Examples:

```python
factorial(5) -> 120
factorial(1) -> 1
factorial(0) -> 1
```

### Issue Type

Logical error

### Notes

The variable `result` is initialized to `0` instead of `1`, causing all multiplication results to remain `0`.

The loop:

```python
range(1, n)
```

does not include `n` itself.

The base case also ignores the valid factorial case for `0`.

---

## Bug 3 - bug3.js

### Intended Behavior

The function should remove non-numeric values and calculate the average of valid numbers.

Example:

```javascript
average([10, "hello", null, 20])
```

Expected output:

```javascript
15.00
```

### Issue Type

Runtime exception and data validation error

### Notes

The condition:

```javascript
typeof n === "number"
```

still allows `NaN`.

The `reduce()` method is called without an initial value, causing a `TypeError` for empty arrays.

The method:

```javascript
toFixed(2)
```

returns a string instead of a number.

---

## Bug 4 - bug4.js

### Intended Behavior

The function should fetch users from an API and return their names in uppercase.

Example output:

```javascript
["LEANNE GRAHAM", "ERVIN HOWELL"]
```

### Issue Type

Incorrect async handling

### Notes

The `fetch()` call is missing `await`.

Incorrect:

```javascript
const response = fetch(url);
```

Correct:

```javascript
const response = await fetch(url);
```

The `response.json()` call also requires `await`.

Without awaiting the Promise, the code attempts to process unresolved asynchronous data.

---

## Bug 5 - bug5.java

### Intended Behavior

The program should count word frequencies and return the most frequently used word.

Example:

```java
"the cat sat on the mat the cat"
```

Expected output:

```java
"the"
```

### Issue Type

NullPointerException and logical error

### Notes

The method does not check whether the input sentence is `null`.

The expression:

```java
counts.get(word) + 1
```

throws a `NullPointerException` because new words do not yet exist in the map.

The comparison operator:

```java
>=
```

may also produce inconsistent tie-breaking behavior.

---

## Bug 6 - bug6.py

### Intended Behavior

The function should read student scores from a CSV file, calculate averages, and write the results to another CSV file.

Expected output columns:

```python
["Name", "Average"]
```

### Issue Type

Type conversion error and resource leak

### Notes

CSV values are read as strings, but `sum()` requires numeric values.

The scores should be converted using `int()` or `float()` before calculating averages.

The files are opened without `with` statements, so files may remain open if an exception occurs.

The output file is also never explicitly closed.
