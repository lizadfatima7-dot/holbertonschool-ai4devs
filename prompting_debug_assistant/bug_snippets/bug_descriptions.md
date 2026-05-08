# Bug Analysis Report

## Bug 1 - bug1.py

### Intended Behavior
The function should return the last `n` elements from a list.

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

This causes the loop to iterate one step beyond the valid list indexes.

When `i` becomes equal to `len(items)`, the function attempts to access an invalid index and raises an `IndexError`.

---

## Bug 2 - bug2.py

### Intended Behavior
The function should calculate and return the factorial of a non-negative integer.

Examples:

```python
factorial(5) -> 120
factorial(0) -> 1
```

### Issue Type
Logical error

### Notes
The base case only handles `n == 1` and ignores the valid case `n == 0`.

The variable:

```python
result = 0
```

is incorrect because factorial multiplication must start from `1`.

The loop:

```python
range(1, n)
```

also excludes `n` from the multiplication.

Because of these problems, the function always returns `0` instead of the correct factorial value.

---

## Bug 3 - bug3.js

### Intended Behavior
The function should remove non-numeric values from an array and return the average of the remaining numeric values rounded to two decimal places.

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
The filter condition:

```javascript
typeof n === "number"
```

still allows `NaN`, because `typeof NaN` returns `"number"`.

The `reduce()` function is called without an initial value, which causes a `TypeError` when the array is empty.

The method:

```javascript
toFixed(2)
```

returns a string instead of a numeric value, which may create problems for later arithmetic operations.

---

## Bug 4 - bug4.js

### Intended Behavior
The function should fetch user data from an API endpoint, convert each username to uppercase, and return an array of uppercase names.

Example:

```javascript
["LEANNE GRAHAM", "ERVIN HOWELL"]
```

The final console output should display the resolved array of names instead of a pending Promise.

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

The call to:

```javascript
response.json()
```

also requires `await`.

Without awaiting these asynchronous operations, the code attempts to use unresolved Promise objects as actual data.

Additionally, the function call:

```javascript
getUserNames(...)
```

is not awaited before logging the result, so the console displays a pending Promise instead of the final array.

---

## Bug 5 - bug5.java

### Intended Behavior
The program should count how many times each word appears in a sentence and return the most frequently occurring word.

Example input:

```java
"the cat sat on the mat the cat"
```

Expected output:

```java
"the"
```

The program should also safely handle invalid input such as `null` values without crashing.

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

also causes a `NullPointerException` because `counts.get(word)` returns `null` for unseen words.

The comparison operator:

```java
>=
```

inside `mostFrequent()` creates inconsistent tie-breaking behavior because later words replace earlier words with the same frequency.

---

## Bug 6 - bug6.py

### Intended Behavior
The function should read student names and scores from a CSV file, calculate the average score for each student, and write the results to a new CSV file.

Expected output columns:

```python
["Name", "Average"]
```

Each row in the output file should contain a student's name and their calculated numeric average.

The program should properly close all files after processing, even if an error occurs.

### Issue Type
Runtime TypeError and resource leak

### Notes
CSV values are read as strings, but the `sum()` function only works with numeric values.

This causes a `TypeError` during average calculation.

The scores should be converted using `int()` or `float()` before calling `sum()`.

The files are opened without using `with` statements:

```python
open(input_path, "r")
```

and

```python
open(output_path, "w")
```

If an exception occurs, the files may remain open and resources may leak.

The output file is also never explicitly closed, which may result in incomplete or corrupted output data.