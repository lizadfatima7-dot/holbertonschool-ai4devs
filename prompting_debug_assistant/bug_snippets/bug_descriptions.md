# Bug Analysis Report

## Bug 1 - bug1.py

Intended Behavior: The function get_last_n accepts a list and integer n and returns only the last n elements of the list.

Issue Type: Off-by-one error.

Notes: The loop uses len(items)+1 causing IndexError when n equals len(items). Fix by using len(items).

## Bug 2 - bug2.py

Intended Behavior: The function factorial accepts a non-negative integer n and returns its factorial value.

Issue Type: Logical error.

Notes: result is set to 0 instead of 1 so all multiplications produce zero. Fix by setting result=1 and using range(1, n+1).

## Bug 3 - bug3.js

Intended Behavior: The function average filters non-numeric values and returns the numeric average rounded to 2 decimal places.

Issue Type: Logical error and type coercion.

Notes: NaN passes the typeof check. reduce crashes on empty array. toFixed returns string. Fix by filtering NaN, adding 0 as initial value, and using parseFloat.

## Bug 4 - bug4.js

Intended Behavior: The function getUserNames asynchronously fetches user objects and returns their names as uppercase strings.

Issue Type: Missing await in asynchronous code.

Notes: fetch and response.json are missing await. The call site does not await either. Fix by adding await before each and at the call site.

## Bug 5 - bug5.java

Intended Behavior: The function countWords counts word frequencies and mostFrequent returns the most frequent word.

Issue Type: Runtime NullPointerException and logical error.

Notes: Null input crashes at toLowerCase. HashMap.get returns null for new words. Fix by adding null guard and using getOrDefault(word, 0)+1.

## Bug 6 - bug6.py

Intended Behavior: The function process_scores reads a CSV of student scores, computes numeric averages, and writes results to a new CSV.

Issue Type: Runtime TypeError and resource leak.

Notes: CSV values are strings so sum raises TypeError. Files are not closed properly. Fix by converting scores with float and using with open.