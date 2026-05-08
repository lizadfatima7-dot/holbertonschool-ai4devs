## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses range(start, len(items) + 1) instead of range(start, len(items)). This causes an IndexError on the last iteration when n equals the length of the list.

## Bug 2 – bug2.py
**Intended Behavior**: Compute the factorial of a non-negative integer.
**Issue Type**: Logical error.
**Notes**: The base case only handles n == 1, missing n == 0. The result is initialized to 0 instead of 1, and the loop range excludes n itself, so the function always returns 0.

## Bug 3 – bug3.js
**Intended Behavior**: Filter non-numeric values from an array and return the average rounded to 2 decimal places.
**Issue Type**: Data type misuse and runtime exception.
**Notes**: typeof NaN === "number" allows NaN to pass the filter. The reduce call has no initial value, causing a TypeError on empty arrays. The toFixed method returns a string, not a number.

## Bug 4 – bug4.js
**Intended Behavior**: Fetch a list of users from an API and return their names in uppercase.
**Issue Type**: Misuse of async/await.
**Notes**: The fetch call is missing await, so response holds a Promise instead of a Response object. Calling .json() on a Promise throws a TypeError. The result is never awaited at the call site.

## Bug 5 – bug5.java
**Intended Behavior**: Count word frequencies in a sentence and return the most frequent word.
**Issue Type**: Runtime NullPointerException and logical error.
**Notes**: No null check exists for the input sentence. HashMap.get() returns null for unseen words, causing a NullPointerException when adding 1. The >= operator makes tie-breaking non-deterministic across HashMap entries.

## Bug 6 – bug6.py
**Intended Behavior**: Read a CSV of student scores, compute each student's average, and write results to a new CSV file.
**Issue Type**: Runtime TypeError and resource leak.
**Notes**: CSV values are strings, so sum() raises a TypeError. Files are opened without a with statement, causing resource leaks if an exception occurs. The output file is never explicitly closed, risking data loss.