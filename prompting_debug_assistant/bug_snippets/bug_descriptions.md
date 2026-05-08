# Bug Analysis Report

---

## Bug 1 - bug1.py

### Intended Behavior
The function `get_last_n(items, n)` must return exactly the last n elements from a list while preserving order.

It must behave like a safe slicing operation without throwing index errors.

Input:
items = [10, 20, 30, 40, 50], n = 3

Output:
[30, 40, 50]

Edge Case:
- If n = 0 → return []
- If n = len(items) → return full list safely

### Issue Type
Off-by-one error

### Notes
The loop uses `len(items) + 1`, which exceeds valid index range.

---

## Bug 2 - bug2.py

### Intended Behavior
The function `factorial(n)` must return the factorial of a non-negative integer using iterative multiplication.

It must correctly compute:
n! = 1 × 2 × ... × n

Input:
n = 5

Output:
120

Edge Case:
- If n = 0 → return 1 (mathematical rule)

### Issue Type
Logical error

### Notes
Result is initialized to 0 instead of 1, which invalidates all multiplication steps.

---

## Bug 3 - bug3.js

### Intended Behavior
The function must return the product of all numeric values in an array while ignoring invalid values.

Input:
[1, 2, 3, 4]

Output:
24

Edge Case:
- Ignore non-numeric values safely

### Issue Type
Logical error and type coercion

### Notes
Product starts at 0 causing incorrect output. Loop boundary may exceed valid index range.

---

## Bug 4 - bug4.js

### Intended Behavior
The function must asynchronously fetch a user by ID and return the user's name.

Input:
id = 1

Output:
John Doe

Edge Case:
- Must wait for async response before accessing data

### Issue Type
Async/await misuse

### Notes
Missing `await` for fetch and JSON parsing causes unresolved Promise usage.

---

## Bug 5 - bug5.java

### Intended Behavior
The function must count word frequency in a sentence and return the most frequent word.

Input:
"the cat sat on the mat the cat"

Output:
"the"

Edge Case:
- If input is null → return safe default (empty or null result)

### Issue Type
NullPointerException and logical error

### Notes
No null check before processing input. New words cause null increment errors in map.

---

## Bug 6 - bug6.py

### Intended Behavior
The function must:
1. Count word frequency in a text
2. Return top N most frequent words
3. Repeat a string N times

Input:
("text text word", 2)

Output:
["text", "word"]

Edge Case:
- N must be a valid integer ≥ 1

### Issue Type
KeyError and TypeError

### Notes
freq[word] causes KeyError on first occurrence. Invalid types for repetition cause runtime errors.