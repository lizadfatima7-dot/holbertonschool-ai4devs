# Bug Analysis Report

---

## Bug 1 - bug1.py

### Intended Behavior
Return the last n elements of a list in correct order without modifying the original list.

The function should behave like a safe slicing operation and must not cause index errors.

Input:
[10, 20, 30, 40, 50], n = 3

Output:
[30, 40, 50]

Edge Case Handling:
If n equals 0 → return empty list []  
If n equals list length → return full list without error

### Issue Type
Off-by-one error

### Notes
The loop uses len(items) + 1, which goes out of range. It should use len(items).

---

## Bug 2 - bug2.py

### Intended Behavior
Compute factorial of a non-negative integer n using iterative multiplication.

The function should correctly multiply all integers from 1 to n.

Input:
n = 5

Output:
120

Edge Case Handling:
If n = 0 → return 1 (by mathematical definition)

### Issue Type
Logical error

### Notes
Result is initialized to 0 instead of 1, which makes all calculations incorrect.

Loop logic does not correctly accumulate factorial values.

---

## Bug 3 - bug3.js

### Intended Behavior
Return the product of all numeric values in an array while ignoring invalid values.

Input:
[1, 2, 3, 4]

Output:
24

Edge Case Handling:
Non-numeric values should be ignored safely.

### Issue Type
Logical error and type coercion

### Notes
Product starts at 0 causing incorrect output. Loop boundary may cause invalid access.

---

## Bug 4 - bug4.js

### Intended Behavior
Fetch a user asynchronously and return the user's name.

Input:
id = 1

Output:
John Doe

Edge Case Handling:
Must wait for API response before accessing data.

### Issue Type
Async/await misuse

### Notes
Missing await for fetch() and response.json(), causing unresolved Promise.

---

## Bug 5 - bug5.java

### Intended Behavior
Count word frequency in a sentence and return the most frequent word.

Input:
"the cat sat on the mat the cat"

Output:
"the"

Edge Case Handling:
If input is null → return empty result or safe default value

### Issue Type
NullPointerException and logical error

### Notes
No null check before processing input. counts.get(word) causes runtime error for new words.

---

## Bug 6 - bug6.py

### Intended Behavior
Count word frequency and return top N most frequent words. Also repeat a string N times.

Input:
("text text word", 2)

Output:
["text", "word"]

Edge Case Handling:
N must be integer; invalid values should be safely converted or rejected.

### Issue Type
KeyError and TypeError

### Notes
freq[word] causes KeyError on first occurrence. Non-integer repetition causes TypeError.