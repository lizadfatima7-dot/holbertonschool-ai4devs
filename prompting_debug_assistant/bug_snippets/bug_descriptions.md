# Bug Analysis Report
This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
Each snippet contains one or more bugs covering syntax errors, logical errors, runtime exceptions, and type misuse.

---

## Bug 1 - bug1.py
**Intended Behavior**: The function get_last_n should accept a list and integer n, then return a new list containing only the last n elements of the original list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses len(items)+1 as upper bound causing IndexError when n equals len(items). Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
**Intended Behavior**: The function factorial should accept a non-negative integer and return its factorial value using iterative multiplication.
**Issue Type**: Logical error.
**Notes**: result is initialized to 0 instead of 1 making every multiplication zero. The loop range excludes n itself and the base case misses n == 0. Fix by setting result=1, using range(1, n+1), and adding n == 0 case.

## Bug 3 - bug3.js
**Intended Behavior**: The function average should filter non-numeric values from an array and return the numeric average of valid numbers rounded to 2 decimal places.
**Issue Type**: Logical error and type coercion.
**Notes**: typeof NaN === "number" allows NaN to pass the filter corrupting the sum. reduce has no initial value causing TypeError on empty arrays. toFixed returns a string not a number. Fix by filtering NaN explicitly, adding initial value 0, and parsing the result.

## Bug 4 - bug4.js
**Intended Behavior**: The function getUserNames should asynchronously fetch a list of users from an API and return their names converted to uppercase.
**Issue Type**: Missing await in asynchronous code.
**Notes**: fetch and response.json are called without await so both return unresolved Promises. Calling .map on a Promise throws TypeError. Fix by adding await before fetch and before response.json and awaiting the function at the call site.

## Bug 5 - bug5.java
**Intended Behavior**: The function countWords should count word frequencies in a sentence and mostFrequent should return the word that appears most often.
**Issue Type**: Runtime NullPointerException and logical error.
**Notes**: No null check exists for the input sentence. HashMap.get returns null for unseen words causing NullPointerException when adding 1. Fix with getOrDefault(word, 0)+1 and add a null guard at the start of countWords.

## Bug 6 - bug6.py
**Intended Behavior**: The function process_scores should read a CSV file of student scores, compute each student average, and write the results to a new CSV output file.
**Issue Type**: Runtime TypeError and resource leak.
**Notes**: CSV values are strings so sum raises TypeError instead of summing numbers. Files are opened without a with statement causing resource leaks on exceptions. Fix by converting scores to float, using with open for both files, and ensuring the output file is properly closed.