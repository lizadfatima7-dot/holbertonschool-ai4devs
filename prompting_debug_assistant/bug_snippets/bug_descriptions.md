# Bug Analysis Report

---

## Bug 1 - bug1.py

### Intended Behavior
Return the last n elements of a list in correct order without modifying the original list.

Input:
- items: list of integers
- n: integer (0 ≤ n ≤ len(items))

Output:
- list containing last n elements

Edge Case:
If n equals the length of the list, return the full list.
If n is 0, return an empty list.

Example:
Input:
[10, 20, 30, 40, 50], n = 3

Output:
[30, 40, 50]

### Issue Type
Off-by-one error

### Notes
Loop uses len(items) + 1 which causes index overflow. Should use len(items).

---

## Bug 2 - bug2.py

### Intended Behavior
Compute the factorial of a non-negative integer n.

Input:
- integer n (n ≥ 0)

Output:
- integer factorial result

Edge Case:
0! must return 1

Example:
Input: 5  
Output: 120

### Issue Type
Logical error

### Notes
Result is initialized to 0 instead of 1, breaking multiplication logic.  
Loop logic does not properly include all required multiplications.

---

## Bug 3 - bug3.js

### Intended Behavior
Return the product of all numeric values in an array.

Input:
[1, 2, 3, 4]

Output:
24

Edge Case:
Ignore non-numeric values safely.

### Issue Type
Logical error and type coercion

### Notes
Product initialized to 0 causing incorrect results.  
Loop boundary may access invalid index.  
Non-numeric values may affect type behavior.

---

## Bug 4 - bug4.js

### Intended Behavior
Fetch user data asynchronously and return the user's name.

Input:
id = 1

Output:
John Doe

Edge Case:
Must wait for async operations before accessing data.

### Issue Type
Async/await misuse

### Notes
Missing await for fetch() and response.json().  
This causes unresolved Promise instead of actual user object.

---

## Bug 5 - bug5.java

### Intended Behavior
Count word frequency in a sentence and return the most frequent word.

Input:
"the cat sat on the mat the cat"

Output:
"the"

Edge Case:
Handle null or empty string safely.

### Issue Type
NullPointerException and logical error

### Notes
No null check before processing input.  
counts.get(word) returns null for new words causing runtime error.

---

## Bug 6 - bug6.py

### Intended Behavior
Count word frequency and return top N words. Also repeat a string N times.

Input:
("text text word", 2)

Output:
["text", "word"]

Edge Case:
N must be integer ≥ 1

### Issue Type
KeyError and TypeError

### Notes
freq[word] causes KeyError on first occurrence.  
Non-integer repetition causes TypeError.  
Fix requires safe dictionary access and type conversion.