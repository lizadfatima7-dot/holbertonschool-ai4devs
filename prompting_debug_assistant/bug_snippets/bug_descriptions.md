# Bug Analysis Report

---

# FILE: bug1.py

## Bug 1 - get_last_n

### Intended Behavior
Return the last n elements of a list while preserving order.

Input:
items = [10, 20, 30, 40, 50], n = 3

Output:
[30, 40, 50]

Edge Case:
- n = 0 → []
- n = len(items) → full list

### Issue Type
Off-by-one error

### Notes
Loop uses len(items) + 1 causing index overflow.

---

# FILE: bug2.py

## Bug 2 - factorial

### Intended Behavior
Compute factorial of a non-negative integer using iteration.

Input:
n = 5

Output:
120

Edge Case:
- n = 0 → 1

### Issue Type
Logical error (incorrect initialization)

### Notes
Result initialized to 0 instead of 1, breaking multiplication logic.

---

# FILE: bug3.js

## Bug 3 - average

### Intended Behavior
Compute average of numeric values in an array while ignoring invalid entries.

Input:
[10, "hello", null, 20]

Output:
15

Edge Case:
- empty or invalid-only arrays should be handled safely

### Issue Type
Type filtering error and runtime exception

### Notes
Non-numeric values are not properly filtered, causing incorrect calculations. Reduce without initial value may fail on empty arrays.

---

# FILE: bug4.js

## Bug 4 - printUser

### Intended Behavior
Fetch user data asynchronously and return the user's name.

Input:
id = 1

Output:
John Doe

Edge Case:
- must wait for async response

### Issue Type
Async/await misuse

### Notes
Missing await for fetch and JSON parsing leads to unresolved Promise usage.

---

# FILE: bug5.java

## Bug 5 - WordCounter

### Intended Behavior
Count word frequency and return most frequent word.

Input:
"the cat sat on the mat the cat"

Output:
"the"

Edge Case:
- null input must be handled safely

### Issue Type
NullPointerException and logical error

### Notes
No null validation. Map increment fails for unseen keys.

---

# FILE: bug6.py

## Bug 6 - top_n_words & multiply_string_times

### Intended Behavior
1. Count word frequency in text  
2. Return top N most frequent words  
3. Repeat string N times

Input:
("text text word", 2)

Output:
["text", "word"]

Edge Case:
- N must be valid integer ≥ 1

### Issue Type
KeyError and TypeError

### Notes
Dictionary access fails for first occurrence. Invalid types cause runtime errors.