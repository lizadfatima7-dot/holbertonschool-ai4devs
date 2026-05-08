# Bug Analysis Report

## Bug 1 - bug1.py

### Intended Behavior
The function should return the last `n` items from a list.

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

This causes the loop to iterate one position beyond the valid list indexes.

When `i == len(items)`, the code accesses an invalid index and raises an `IndexError`.

---

## Bug 2 - bug2.py

### Intended Behavior
The function should compute and return the factorial of a non-negative integer.

Examples:

```python
factorial(5) -> 120
factorial(0) -> 1
```

### Issue Type
Logical error

### Notes
The base case only handles `n == 1`, missing the valid case `n == 0`.

The variable `result` is initialized to `0` instead of `1`, causing all multiplications to remain `0`.

The loop:

```python
range(1, n)
```

does not include `n` itself in the multiplication.

Because of these issues, the function always returns `0`.

---

## Bug 3 - bug3.js

### Intended Behavior
The function should filter non-numeric values from an array and return the average of the remaining numeric values rounded to 2 decimal places.

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
The condition:

```javascript
typeof n === "number"
```

still allows `NaN`, because `typeof NaN` is `"number"`.

The `reduce()` method is used without an initial value, so calling the function with an empty array throws a `TypeError`.

The method:

```javascript
toFixed(2)
```

returns a string instead of a numeric value, which may create issues in later calculations.

---

## Bug 4 - bug4.js

### Intended Behavior
The function should fetch user data from an API and return an array of uppercase user names.

Example output:

```javascript
["LEANNE GRAHAM", "ERVIN HOWELL"]
```

### Issue Type
Misuse of async/await

### Notes
The `fetch()` call is missing `await`.

Incorrect code:

```javascript
const response = fetch(url);
```

Correct code:

```javascript
const response = await fetch(url);
```

The `response.json()` call also requires `await`.

Without awaiting these asynchronous operations, the code attempts to use Promise objects as actual data, causing runtime errors.

Additionally, the returned result is not awaited at the call site, so the console displays a pending Promise instead of the resolved array.

---

## Bug 5 - bug5.java

### Intended Behavior
The program should count the frequency of words in a sentence and return the most frequently occurring word.

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
The method does not check whether the input sentence is `null`.

Calling:

```java
sentence.toLowerCase()
```

when `sentence` is `null` throws a `NullPointerException`.

The expression:

```java
counts.get(word) + 1
```

also throws a `NullPointerException` for words that are not yet stored in the map because `counts.get(word)` returns `null`.

The comparison operator:

```java
>=
```

inside `mostFrequent()` creates inconsistent tie-breaking behavior because later words replace earlier words with the same frequency.

---

## Bug 6 - bug6.py

### Intended Behavior
The function should read student names and scores from a CSV file, calculate each student's average score, and write the results to another CSV file.

Expected output columns:

```python
["Name", "Average"]
```

### Issue Type
Runtime TypeError and resource leak

### Notes
CSV values are read as strings, but the `sum()` function requires numeric values.

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

The output file is also never explicitly closed, which can lead to incomplete or corrupted output data.