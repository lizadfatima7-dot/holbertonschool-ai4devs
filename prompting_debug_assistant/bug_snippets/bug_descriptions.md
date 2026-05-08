# Bug Analysis Report

## Bug 1 - bug1.py

### Intended Behavior
Return the last n elements of a list in correct order.

Input:
[10, 20, 30, 40, 50], n = 3

Output:
[30, 40, 50]

### Issue Type
Off-by-one error

### Notes
Loop uses len(items) + 1 causing index overflow. Should use len(items).

---

## Bug 2 - bug2.py

### Intended Behavior
Calculate the factorial of a non-negative integer n.

Input:
n = 5

Output:
120

Edge case:
n = 0 should return 1

### Issue Type
Logical error

### Notes
Result initialized to 0 instead of 1, causing all results to be 0. Loop logic is also incorrect and misses proper accumulation.

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
Product initialized to 0 causing incorrect output. Loop boundary may access invalid index. Type coercion may occur with non-numeric values.

---

## Bug 4 - bug4.js

### Intended Behavior
Fetch user data asynchronously and print the user's name.

Input:
id = 1

Output:
John Doe

### Issue Type
Async/await misuse

### Notes
Missing await for fetch() and response.json(), causing unresolved Promise instead of actual user object.

---

## Bug 5 - bug5.java

### Intended Behavior
Count word frequency in a sentence and return the most frequent word.

Input:
"the cat sat on the mat the cat"

Output:
"the"

### Issue Type
NullPointerException and logical error

### Notes
No null check for input string. counts.get(word) returns null for new words causing runtime error when incrementing.

---

## Bug 6 - bug6.py

### Intended Behavior
Count word frequency in a sentence and return top N most frequent words. Also repeat a string N times.

Input:
("text text word", 2)

Output:
["text", "word"]

### Issue Type
KeyError and TypeError

### Notes
freq[word] causes KeyError for first occurrence. Non-integer repetition causes TypeError. Use safe dictionary access and cast input to int.