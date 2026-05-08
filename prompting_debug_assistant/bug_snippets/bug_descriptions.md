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
- n = 0 → return []
- n = len(items) → return full list safely

### Issue Type
Off-by-one error

### Notes
Loop uses len(items) + 1 which causes index overflow.

---

# FILE: bug2.py

## Bug 2 - factorial

### Intended Behavior
Compute factorial of a non-negative integer using iterative multiplication.

Input:
n = 5

Output:
120

Edge Case:
- n = 0 → return 1

### Issue Type
Logical error

### Notes
Result initialized to 0 instead of 1, breaking multiplication logic.

---

# FILE: bug3.js

## Bug 3 - productOfArray

### Intended Behavior
Return product of all numeric values in an array.

Input:
[1, 2, 3, 4]

Output:
24

Edge Case:
- ignore non-numeric values

### Issue Type
Logical error and type coercion

### Notes
Product starts at 0 causing incorrect result. Loop boundary may exceed array length.

---

# FILE: bug4.js

## Bug 4 - printUser

### Intended Behavior
Fetch user asynchronously and return user name.

Input:
id = 1

Output:
John Doe

Edge Case:
- must wait for async response before accessing data

### Issue Type
Async/await misuse

### Notes
Missing await for fetch and JSON parsing causes unresolved Promise.

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
- null input → safe handling required

### Issue Type
NullPointerException and logical error

### Notes
No null check. Map increment fails for new words.

---

# FILE: bug6.py

## Bug 6 - top_n_words & multiply_string_times

### Intended Behavior
1. Count word frequency in text  
2. Return top N words  
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
freq[word] causes KeyError. Invalid types cause runtime errors.