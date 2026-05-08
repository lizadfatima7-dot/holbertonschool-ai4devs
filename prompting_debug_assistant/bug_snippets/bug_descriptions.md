# Bug Analysis Report

---

# FILE: bug1.py

## BUG 1 - get_last_n

### Intended Behavior
The function must return the last n elements of a list in correct order without modifying the original list.

Specification:
- Input: list of integers, integer n
- Output: list containing last n elements
- Behavior must not raise index errors

Input:
[10, 20, 30, 40, 50], n = 3

Expected Output:
[30, 40, 50]

Edge Case Handling:
- n = 0 → return []
- n = len(list) → return full list safely

### Issue Type
Off-by-one error

### Notes
Loop uses len(items) + 1 causing index overflow.

---

# FILE: bug2.py

## BUG 2 - factorial

### Intended Behavior
The function must compute factorial of a non-negative integer using iterative multiplication.

Specification:
- Input: integer n (n ≥ 0)
- Output: n! value

Input:
n = 5

Expected Output:
120

Edge Case Handling:
- n = 0 → return 1

### Issue Type
Logical error (incorrect initialization)

### Notes
Result initialized to 0 instead of 1, breaking multiplication logic.

---

# FILE: bug3.js

## BUG 3 - average

### Intended Behavior
The function must compute the average of numeric values in an array while ignoring invalid entries.

Specification:
- Input: array of mixed values
- Output: numeric average

Input:
[10, "hello", null, 20]

Expected Output:
15

Edge Case Handling:
- empty array → must be safely handled

### Issue Type
Type filtering error and runtime exception risk

### Notes
Non-numeric values are not correctly filtered. Reduce operation may fail on empty arrays.

---

# FILE: bug4.js

## BUG 4 - printUser

### Intended Behavior
The function must asynchronously fetch user data by ID and return the user's name.

Specification:
- Input: user ID
- Output: string username

Input:
id = 1

Expected Output:
John Doe

Edge Case Handling:
- must await API response before processing

### Issue Type
Async/await misuse

### Notes
Missing await for fetch and JSON parsing leads to unresolved Promise usage.

---

# FILE: bug5.java

## BUG 5 - WordCounter

### Intended Behavior
The function must count word frequency in a sentence and return the most frequent word.

Specification:
- Input: string sentence
- Output: most frequent word

Input:
"the cat sat on the mat the cat"

Expected Output:
"the"

Edge Case Handling:
- null input → safe handling required

### Issue Type
NullPointerException and logical error

### Notes
No null validation before processing input. Map increment fails for unseen keys.

---

# FILE: bug6.py

## BUG 6 - top_n_words & multiply_string_times

### Intended Behavior
The system must:
1. Count word frequency in text
2. Return top N most frequent words
3. Repeat string N times safely

Specification:
- Input: text, integer N
- Output: list of top words

Input:
("text text word", 2)

Expected Output:
["text", "word"]

Edge Case Handling:
- N must be integer ≥ 1

### Issue Type
KeyError and TypeError

### Notes
Dictionary access fails for first occurrence. Invalid input types cause runtime errors.