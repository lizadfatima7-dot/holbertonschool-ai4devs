# Bug Analysis Report

## Bug 1 - bug1.py

### Intended Behavior
Return the last n elements from a list in correct order.

Input:
- list of integers
- integer n

Output:
- list containing last n elements

Example:
get_last_n([10, 20, 30, 40, 50], 3)

Expected output:
[30, 40, 50]

### Issue Type
Off-by-one error

### Notes
The loop uses len(items) + 1, which causes an index out of range error. It should use len(items).

---

## Bug 2 - bug2.py

### Intended Behavior
Compute the average of only positive numbers in a list.

Input:
[1, -2, 3, 4]

Output:
2.67

### Issue Type
Logical error

### Notes
The count variable includes all numbers instead of only positive ones, causing incorrect average calculation.

---

## Bug 3 - bug3.js

### Intended Behavior
Return the product of all numeric elements in an array.

Input:
[1, 2, 3, 4]

Output:
24

### Issue Type
Logical error and type coercion

### Notes
Product is initialized to 0, which makes result always 0. Loop boundary is incorrect and may cause invalid access.

---

## Bug 4 - bug4.js

### Intended Behavior
Fetch a user asynchronously and print the user’s name.

Input:
id = 1

Output:
John Doe

### Issue Type
Async/await misuse

### Notes
Missing await for fetch() and response.json(), causing unresolved Promise instead of actual data.

---

## Bug 5 - bug5.java

### Intended Behavior
Reverse an integer array in-place.

Input:
[1, 2, 3]

Output:
[3, 2, 1]

### Issue Type
Syntax error and off-by-one error

### Notes
Missing semicolon prevents compilation. Array indexing goes out of bounds due to incorrect formula.

---

## Bug 6 - bug6.py

### Intended Behavior
Count word frequency and return top N words. Also repeat a string N times.

Input:
("text text word", 2)

Output:
["text", "word"]

### Issue Type
KeyError and TypeError

### Notes
Accessing freq[word] before initialization causes KeyError. Non-integer repetition causes TypeError. Use safe dictionary access and convert input to int.