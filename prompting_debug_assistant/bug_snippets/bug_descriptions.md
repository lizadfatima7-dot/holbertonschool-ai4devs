# Bug Analysis Report

## Bug 1 - bug1.py

### Intended Behavior

The function should return the last `n` items from a list without causing an error.

Example input:

```python
get_last_n([10, 20, 30, 40, 50], 3)
```

Expected output:

```python
[30, 40, 50]
```

The function should also work correctly when `n` is equal to the length of the list.

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

This causes the loop to iterate one step beyond the final valid index.

When `i == len(items)`, the code accesses an invalid list index and raises an `IndexError`.

---

## Bug 2 - bug2.py

### Intended Behavior

The function should correctly compute the factorial of any non-negative integer.

Examples:

```python
factorial(5) -> 120
factorial(1) -> 1
factorial(0) -> 1
```

The function should multiply all integers from `1` through `n` and return the correct factorial value.

### Issue Type

Logical error

### Notes

The base case only checks:

```python
if n == 1:
```

and does not handle the valid factorial case for `0`.

The variable:

```python
result = 0
```

is incorrect because factorial multiplication must begin with `1`.

The loop:

```python
range(1, n)
```

does not include `n`, so the final multiplication step is skipped.

Because of these issues, the function always returns `0` instead of the correct factorial result.

---

## Bug 3 - bug3.js

### Intended Behavior

The function should ignore non-numeric values, calculate the average of valid numeric entries, and return the result rounded to two decimal places.

Example input:

```javascript
average([10, "hello", null, 20])
```

Expected output:

```javascript
15.00
```

The function should also safely handle empty arrays without crashing.

### Issue Type

Data type misuse and runtime exception

### Notes

The filter condition:

```javascript
typeof n === "number"
```

still allows `NaN`, because `typeof NaN` returns `"number"`.

The `reduce()` function is called without an initial value, which causes a `TypeError` when the filtered array is empty.

The method:

```javascript
toFixed(2)
```

returns a string rather than a numeric value, which may create problems in later calculations.

---

## Bug 4 - bug4.js

### Intended Behavior

The function should fetch user data from an API, convert all usernames to uppercase, and return an array of uppercase names.

Example output:

```javascript
["LEANNE GRAHAM", "ERVIN HOWELL"]
```

The function should wait for the API response and JSON conversion before processing the data.

The final console output should display the completed array of names instead of a pending Promise.

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

The following line also requires `await`:

```javascript
response.json()
```

Without awaiting these asynchronous operations, the code attempts to process unresolved Promise objects as real data.

Additionally, the result of:

```javascript
getUserNames(...)
```

is not awaited before printing, so the console displays a pending Promise instead of the resolved array.

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

The program should safely handle empty or null input values without throwing exceptions.

The word counting logic should correctly initialize counts for new words before incrementing them.

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

also throws a `NullPointerException` because `counts.get(word)` returns `null` for words that have not yet been added to the map.

The comparison operator:

```java
>=
```

inside `mostFrequent()` causes inconsistent tie-breaking behavior because later words replace earlier words when frequencies are equal.

---

## Bug 6 - bug6.py

### Intended Behavior

The function should read student names and scores from a CSV file, calculate each student's average score, and write the results to a new CSV file.

Expected output columns:

```python
["Name", "Average"]
```

Each output row should contain a student's name and their correctly calculated numeric average.

The function should safely close all opened files after processing, even if an error occurs during execution.

### Issue Type

Runtime TypeError and resource leak

### Notes

CSV values are read as strings, but the `sum()` function only works with numeric values.

This causes a `TypeError` during average calculation.

The score values should be converted using `int()` or `float()` before calling `sum()`.

The files are opened using:

```python
open(input_path, "r")
```

and:

```python
open(output_path, "w")
```

without `with` statements.

If an exception occurs, the files may remain open and system resources may leak.

The output file is also never explicitly closed, which may result in incomplete or corrupted output data.
