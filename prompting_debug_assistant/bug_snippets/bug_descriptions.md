# Bug Analysis Report

This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
Each snippet contains one or more bugs covering syntax errors, logical errors, runtime exceptions, and type misuse.

---

## Bug 1 - bug1.py

### Intended Behavior
The function get_last_n should accept a list and integer n, then return a new list containing only the last n elements of the original list. Given [10, 20, 30, 40, 50] and n=3 the expected output is [30, 40, 50]. Given n=5 the expected output is [10, 20, 30, 40, 50].

### Issue Type
Off-by-one error.

### Error Message
IndexError: list index out of range

### Notes
The loop uses range(start, len(items)+1) which goes one index past the end of the list. On the final iteration items[i] accesses an index equal to len(items) which does not exist. Fix by changing len(items)+1 to len(items) in the range call.

---

## Bug 2 - bug2.py

### Intended Behavior
The function factorial should accept a non-negative integer n and return its factorial value using an iterative loop. Expected outputs: factorial(0) returns 1, factorial(1) returns 1, factorial(5) returns 120.

### Issue Type
Logical error.

### Error Message
No exception is raised. The function silently returns 0 for all inputs greater than 1.

### Notes
result is initialized to 0 instead of 1 so every multiplication produces zero. The loop uses range(1, n) which excludes n so the last factor is never included. The base case only checks n==1 and misses n==0. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

---

## Bug 3 - bug3.js

### Intended Behavior
The function average should accept an array of mixed values, filter out non-numeric entries, compute the mean of the remaining valid numbers, and return it rounded to 2 decimal places as a number. Expected output for [1, 2, 3, 4, 5] is 3.00. Expected output for [10, hello, null, 20] is 15.00.

### Issue Type
Logical error and type coercion.

### Error Message
TypeError: Reduce of empty array with no initial value

### Notes
typeof NaN equals number in JavaScript so NaN passes the filter and corrupts the result. reduce throws TypeError when called on an empty array without an initial value. toFixed returns a string so downstream arithmetic produces wrong results. Fix by filtering out NaN with isNaN, passing 0 as initial value to reduce, and returning parseFloat of the toFixed result.

---

## Bug 4 - bug4.js

### Intended Behavior
The function getUserNames should asynchronously fetch a list of user objects from a URL, extract the name field from each user object, convert each name to uppercase, and return the array of uppercase strings. Expected output is an array like [USER ONE, USER TWO, ...].

### Issue Type
Missing await in asynchronous code.

### Error Message
TypeError: response.json is not a function

### Notes
fetch is called without await so response holds an unresolved Promise instead of a Response object. Calling json on a Promise throws TypeError. The call site does not await the async function so result is always Promise pending. Fix by adding await before fetch, adding await before response.json, and awaiting the function at the call site.

---

## Bug 5 - bug5.java

### Intended Behavior
The function countWords should split a sentence into words and return a map of each word to its frequency count. The function mostFrequent should return the word with the highest count. For the sentence the cat sat on the mat the cat the expected output is the with frequency 3.

### Issue Type
Runtime NullPointerException and logical error.

### Error Message
NullPointerException at sentence.toLowerCase() when null is passed, and NullPointerException at counts.get(word)+1 for the first occurrence of any word.

### Notes
No null guard exists before calling toLowerCase on the sentence. HashMap.get returns null for words not yet added causing NullPointerException when adding 1. The >= comparison produces non-deterministic results on ties because HashMap order is undefined. Fix by adding a null check, using getOrDefault(word, 0)+1, and changing >= to >.

---

## Bug 6 - bug6.py

### Intended Behavior
The function process_scores should read a CSV where each row has a student name followed by numeric scores, compute the numeric average of those scores, and write a new CSV with columns Name and Average. For a row like Alice,80,90,100 the expected output row is Alice,90.0.

### Issue Type
Runtime TypeError and resource leak.

### Error Message
TypeError: unsupported operand type(s) for +: int and str

### Notes
CSV parsing returns all values as strings so scores contains strings not numbers and sum raises TypeError. Each score must be converted with float before summing. Both files are opened without a with statement so handles are not closed if an exception occurs. The output file is never explicitly closed risking data not being flushed. Fix by converting each score with float and using with open for both files.