## Bug 1 – bug1.py
**Intended Behavior**: The function should return a new list containing only the last n elements of the input list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses len(items)+1 as upper bound which causes an IndexError. Replace len(items)+1 with len(items) to fix the boundary.

## Bug 2 – bug2.py
**Intended Behavior**: The function should return the factorial of n as the product of all integers from 1 to n, with factorial(0) returning 1.
**Issue Type**: Logical error.
**Notes**: Result is initialized to 0 instead of 1, making all products zero, and the range excludes n. Set result=1 and use range(1, n+1).

## Bug 3 – bug3.js
**Intended Behavior**: The function should filter non-numeric values from an array and return the arithmetic mean rounded to 2 decimal places.
**Issue Type**: Off-by-one error / Logic error.
**Notes**: typeof NaN returns number so it passes the filter, and reduce lacks an initial value. Use Number.isNaN and provide 0 as the initial value.

## Bug 4 – bug4.js
**Intended Behavior**: The async function should fetch a JSON array of user objects from a URL and return each user name converted to uppercase.
**Issue Type**: Misuse of data types or libraries.
**Notes**: Both fetch and response.json return Promises but are not awaited, causing errors when mapping. Add the await keyword before each call.

## Bug 5 – bug5.java
**Intended Behavior**: The function should count word frequencies in a sentence and return the most frequent word.
**Issue Type**: Runtime exception.
**Notes**: Null inputs and HashMap.get returning null for unseen words cause NullPointerExceptions. Add a null guard and use getOrDefault(word, 0)+1.

## Bug 6 – bug6.py
**Intended Behavior**: The function should read student names and scores from a CSV, compute averages, and write results to a new CSV.
**Issue Type**: Misuse of data types or libraries.
**Notes**: CSV values are read as strings, so sum() raises a TypeError. Convert scores using float() and ensure files are closed using with-blocks.