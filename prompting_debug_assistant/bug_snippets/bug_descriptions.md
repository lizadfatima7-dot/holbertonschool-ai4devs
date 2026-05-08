# Bug Analysis Report

## Bug 1 - bug1.py

### Intended Behavior

The function is intended to return the last `n` elements from a list while preserving their original order.

For example:

```python id="7aj4tm"
get_last_n([10, 20, 30, 40, 50], 3)
```

should return:

```python id="w9ub2n"
[30, 40, 50]
```

The function should also correctly handle edge cases where `n` equals the size of the list.

### Issue Type

Off-by-one error

### Notes

The loop uses:

```python id="4bfhzc"
range(start, len(items) + 1)
```

instead of:

```python id="dz7f3h"
range(start, len(items))
```

This causes the loop to iterate one step beyond the valid index range.

When the loop reaches `len(items)`, the code attempts to access an invalid list index, producing an `IndexError`.

As a result, the function crashes instead of returning the expected list.

---

## Bug 2 - bug2.py

### Intended Behavior

The function is intended to calculate the factorial of a non-negative integer.

For example:

```python id="kr54hz"
factorial(5)
```

should return:

```python id="d9k89z"
120
```

and:

```python id="jlwm3x"
factorial(0)
```

should return:

```python id="a2u5yj"
1
```

The function should multiply all integers from `1` through `n` and return the final product.

### Issue Type

Logical error

### Notes

The variable:

```python id="flz2s7"
result = 0
```

is incorrect because factorial multiplication must start from `1`.

The loop:

```python id="7d5ehv"
range(1, n)
```

does not include the value `n`, so the multiplication is incomplete.

The base case only handles:

```python id="sn9j3w"
n == 1
```

and ignores the valid factorial case for `0`.

Because of these issues, the function always returns `0` instead of the correct factorial value.

---

## Bug 3 - bug3.js

### Intended Behavior

The function is intended to filter out non-numeric values from an array, calculate the average of the remaining numeric values, and return the result rounded to two decimal places.

For example:

```javascript id="bx6l6x"
average([10, "hello", null, 20])
```

should return:

```javascript id="0w8jlwm"
15.00
```

The function should also safely handle edge cases such as empty arrays or arrays containing invalid numeric values.

### Issue Type

Runtime exception and data validation error

### Notes

The condition:

```javascript id="w5q6of"
typeof n === "number"
```

still allows `NaN`, because JavaScript evaluates:

```javascript id="lhm2xw"
typeof NaN
```

as `"number"`.

The `reduce()` function is called without an initial value, causing a `TypeError` when the filtered array is empty.

The method:

```javascript id="vlr41g"
toFixed(2)
```

returns a string instead of a numeric value, which may create problems for later calculations.

As a result, the function may crash or return values with incorrect data types.

---

## Bug 4 - bug4.js

### Intended Behavior

The function is intended to fetch user data from an API endpoint, extract each user's name, convert the names to uppercase, and return them as an array.

Example expected output:

```javascript id="y8mjlwm"
["LEANNE GRAHAM", "ERVIN HOWELL"]
```

The function should wait for the API request and JSON parsing to finish before attempting to process the data.

The final console output should display the resolved array rather than a pending Promise object.

### Issue Type

Incorrect async handling

### Notes

The statement:

```javascript id="9kme8o"
const response = fetch(url);
```

does not use `await`, so `response` becomes a Promise instead of the actual HTTP response.

The call to:

```javascript id="ekc12p"
response.json()
```

also requires `await`.

Without awaiting these asynchronous operations, the program attempts to use unresolved Promise objects as real data, causing runtime errors.

Additionally, the result of:

```javascript id="gx4u9x"
getUserNames(...)
```

is logged without `await`, so the console displays a pending Promise instead of the completed array.

---

## Bug 5 - bug5.java

### Intended Behavior

The program is intended to count the frequency of each word in a sentence and return the word that appears most often.

For example:

```java id="8ydh67"
"the cat sat on the mat the cat"
```

should produce:

```java id="uxoqxl"
"the"
```

The program should also safely handle invalid input such as `null` values and correctly initialize counts for newly encountered words.

### Issue Type

NullPointerException and logical error

### Notes

The method does not verify whether the input sentence is `null`.

Calling:

```java id="h0g1pt"
sentence.toLowerCase()
```

when the input is `null` throws a `NullPointerException`.

The expression:

```java id="ux6e1t"
counts.get(word) + 1
```

also throws a `NullPointerException` because new words do not yet exist in the map.

The comparison operator:

```java id="tpk2z4"
>=
```

inside `mostFrequent()` creates inconsistent tie-breaking behavior because later words can replace earlier words with the same frequency.

As a result, the program may crash or produce inconsistent outputs.

---

## Bug 6 - bug6.py

### Intended Behavior

The function is intended to read student names and scores from a CSV file, calculate each student's average score, and write the results to another CSV file.

The output file should contain:

```python id="8ofc0n"
["Name", "Average"]
```

Each row should store a student's name together with the calculated numeric average.

The function should also properly close all opened files, even when errors occur during processing.

### Issue Type

Type conversion error and resource leak

### Notes

CSV values are read as strings, but the `sum()` function requires numeric values.

As a result, the statement that calculates the average raises a `TypeError`.

The scores should first be converted using `int()` or `float()` before arithmetic operations are performed.

The files are opened without using `with` statements:

```python id="r7y1g7"
open(input_path, "r")
```

and:

```python id="jlwm8u"
open(output_path, "w")
```

If an exception occurs, the files may remain open and system resources may leak.

The output file is also never explicitly closed, which may result in incomplete or corrupted CSV output.
