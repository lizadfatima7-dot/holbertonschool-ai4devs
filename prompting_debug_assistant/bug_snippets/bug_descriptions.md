# Bug Analysis Report

---

# FILE: bug1.py

## BUG 1 - get_last_n

### Intended Behavior
Function must return the last n elements of a list in correct order.

Specification:
- Input: list of integers, integer n
- Output: list of last n elements
- Must not raise index errors

Input:
[10, 20, 30, 40, 50], n = 3

Expected Output:
[30, 40, 50]

Edge Case Handling:
- n = 0 → []
- n = len(list) → full list

### Issue Type
Off-by-one error

### Notes
Loop exceeds valid index range due to len(items) + 1.

---

# FILE: bug2.py

## BUG 2 - factorial

### Intended Behavior
Function must compute factorial of a non-negative integer using iterative multiplication.

Specification:
- Input: integer n (n ≥ 0)
- Output: factorial result

Input:
n = 5

Expected Output:
120

Edge Case Handling:
- n = 0 → 1

### Issue Type
Logical error (incorrect initialization)

### Notes
Result initialized to 0 instead of 1 causing invalid multiplication.

---

# FILE: bug3.js

## BUG 3 - average

### Intended Behavior
Function must compute average of numeric values in an array while ignoring invalid entries.

Specification:
- Input: mixed array
- Output: numeric average

Input:
[10, "hello", null, 20]

Expected Output:
15

Edge Case Handling:
- empty array → safe handling required

### Issue Type
Type filtering error and runtime exception risk

### Notes
Non-numeric values not properly filtered. Reduce may fail on empty arrays.

---

# FILE: bug4.js

## BUG 4 - printUser

### Intended Behavior
Function must fetch user data asynchronously and return username.

Specification:
- Input: user ID
- Output: string username

Input:
id = 1

Expected Output:
John Doe

Edge Case Handling:
- must await async operations

### Issue Type
Async/await misuse

### Notes
Missing await in fetch and JSON parsing results in unresolved Promise.

---

# FILE: bug5.java

## BUG 5 - WordCounter

### Intended Behavior
Function must return the most frequent word in a sentence.

Specification:
- Input: string sentence
- Output: most frequent word

Input:
"the cat sat on the mat the cat"

Expected Output:
"the"

Edge Case Handling:
- null input → safe default handling required

### Issue Type
NullPointerException and logical error

### Notes
No null validation before processing. Map operations fail for new keys.

---

# FILE: bug6.py

## BUG 6 - Multi-function module (top_n_words + multiply_string_times)

### Intended Behavior
This file contains two functions:

1. top_n_words:
- Count word frequency in text
- Return top N most frequent words

2. multiply_string_times:
- Repeat a string N times

Specification:
- Input: text + integer N OR string + integer N
- Output: list or repeated string depending on function

Input:
("text text word", 2)

Expected Output:
["text", "word"]

Edge Case Handling:
- N must be integer ≥ 1
- invalid types must be safely handled

### Issue Type
KeyError and TypeError

### Notes
Dictionary access fails on first occurrence. Invalid types cause runtime errors.