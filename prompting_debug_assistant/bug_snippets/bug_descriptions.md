# Bug Analysis Report
This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
Each snippet contains one or more bugs covering syntax errors, logical errors, runtime exceptions, and type misuse.

---

## Bug 1 - bug1.py
**Intended Behavior**: The function get_last_n should accept a list and integer n, then return a new list containing only the last n elements of the original list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses len(items)+1 as upper bound causing IndexError when n equals len(items). Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
**Intended Behavior**: The function factorial should accept a non-negative integer n and return its factorial by multiplying all integers from 1 to n inclusively using an iterative loop.
**Issue Type**: Logical error.
**Notes**: result is initialized to 0 instead of 1 making every multiplication produce zero. The loop uses range(1, n) which excludes n itself. The base case misses n == 0. Fix by setting result=1, using range(1, n+1), and adding if n == 0 return 1.

## Bug 3 - bug3.js
**Intended Behavior**: The function average should filter out non-numeric values from an array and return the numeric average of the remaining valid numbers rounded to 2 decimal places.
**Issue Type**: Logical error and type coercion.
**Notes**: typeof NaN === "number" allows NaN to pass the filter and corrupt the sum. reduce has no initial value causing TypeError on empty arrays. toFixed returns a string not a number. Fix by adding isNaN check, passing 0 as initial value to reduce, and wrapping result in parseFloat.

## Bug 4 - bug4.js
**Intended Behavior**: The function getUserNames should asynchronously fetch a list of user objects from a given API URL and return an array of their names converted to uppercase strings.
**Issue Type**: Missing await in asynchronous code.
**Notes**: fetch is called without await so response holds an unresolved Promise instead of a Response object. Calling .json() on a Promise throws TypeError. The call site does not await the function so result is always Promise pending. Fix by adding await before fetch and before response.json and awaiting the function at the call site.

## Bug 5 - bug5.java
**Intended Behavior**: The function countWords should count how many times each word appears in a given sentence and mostFrequent should return the word with the highest frequency count from the resulting map.
**Issue Type**: Runtime NullPointerException and logical error.
**Notes**: No null check exists for the input sentence so passing null throws NullPointerException immediately. HashMap.get returns null for words not yet in the map causing NullPointerException when adding 1. Fix by adding a null guard at the start, using getOrDefault(word, 0)+1, and changing >= to >.

## Bug 6 - bug6.py
**Intended Behavior**: The function process_scores should open a CSV file where each row contains a student name followed by a list of numeric scores, compute the numeric average of those scores for each student, and write a new CSV file containing each student name alongside their computed average.
**Issue Type**: Runtime TypeError and resource leak.
**Notes**: CSV row values are read as strings not numbers so scores is expected to be a list of numeric values but CSV parsing returns strings by default causing sum to raise TypeError. Each score must be converted with float before summing. Both files are opened without a with statement causing resource leaks if an exception occurs. The output file is never explicitly closed risking data not being flushed to disk. Fix by converting each score with float and using with open for both files.