# Bug Analysis Report

This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
Each snippet contains one or more bugs covering syntax errors, logical errors, runtime exceptions, and type misuse.

---

## Bug 1 - bug1.py

### Intended Behavior
The function get_last_n should accept a list and integer n, then return a new list containing only the last n elements of the original list. For example given [10, 20, 30, 40, 50] and n=3 the expected output is [30, 40, 50].

### Issue Type
Off-by-one error.

### Notes
The loop uses range(start, len(items)+1) which goes one index past the end of the list causing IndexError on the last iteration. Fix by changing len(items)+1 to len(items) in the range call.

---

## Bug 2 - bug2.py

### Intended Behavior
The function factorial should accept a non-negative integer n and return its factorial value. For example factorial(5) should return 120 and factorial(0) should return 1.

### Issue Type
Logical error.

### Notes
result is initialized to 0 instead of 1 so every multiplication produces zero. The loop uses range(1, n) which excludes n itself. The base case misses n==0. Fix by setting result=1, using range(1, n+1), and adding a return 1 when n equals 0.

---

## Bug 3 - bug3.js

### Intended Behavior
The function average should accept an array of mixed values, filter out non-numeric values, compute the mean of valid numbers, and return it rounded to 2 decimal places as a number. For example average([1, 2, 3, 4, 5]) should return 3.00.

### Issue Type
Logical error and type coercion.

### Notes
typeof NaN equals number in JavaScript so NaN passes the filter and corrupts the sum. reduce has no initial value causing TypeError on empty arrays. toFixed returns a string not a number. Fix by adding isNaN check, passing 0 to reduce, and returning parseFloat of the result.

---

## Bug 4 - bug4.js

### Intended Behavior
The function getUserNames should asynchronously fetch a list of user objects from a given URL, extract the name from each user, convert it to uppercase, and return the array of uppercase name strings.

### Issue Type
Missing await in asynchronous code.

### Notes
fetch is called without await so response holds an unresolved Promise instead of a Response object. Calling json on a Promise throws TypeError. The call site does not await the function so result is always a pending Promise. Fix by adding await before fetch and before response.json and awaiting the call site.

---

## Bug 5 - bug5.java

### Intended Behavior
The function countWords should accept a sentence, split it into words, and return a map of each word to its frequency. The function mostFrequent should return the word with the highest count. For the sentence the cat sat on the mat the cat the expected result is the with count 3.

### Issue Type
Runtime NullPointerException and logical error.

### Notes
No null check exists so passing null throws NullPointerException immediately. HashMap.get returns null for unseen words causing NullPointerException when adding 1. The >= comparison gives non-deterministic results on ties. Fix by adding a null guard, using getOrDefault(word, 0)+1, and changing >= to >.

---

## Bug 6 - bug6.py

### Intended Behavior
The function process_scores should read a CSV file where each row contains a student name and numeric scores, compute the average of those numeric scores, and write a new CSV file with columns Name and Average containing each student result.

### Issue Type
Runtime TypeError and resource leak.

### Notes
CSV values are read as strings not numbers so scores contains strings by default and calling sum raises TypeError. Each score must be converted with float before summing. Both files are opened without a with statement causing resource leaks on exceptions. The output file is never closed risking data loss. Fix by converting scores with float and using with open for both files.