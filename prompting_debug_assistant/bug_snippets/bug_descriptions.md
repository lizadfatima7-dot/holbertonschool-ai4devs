## Bug 1 – bug1.py
**Intended Behavior**: The function should return a new list containing only the last n elements of the input list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses len(items)+1 as upper bound causing IndexError. Replace len(items)+1 with len(items) to fix.

## Bug 2 – bug2.py
**Intended Behavior**: The function should return the factorial of n as the product of all integers from 1 to n.
**Issue Type**: Logical error.
**Notes**: Result is initialized to 0 instead of 1, and the range excludes n. Set result=1 and use range(1, n+1).

## Bug 3 – bug3.js
**Intended Behavior**: The function should filter non-numeric values and return the arithmetic mean rounded to 2 decimal places.
**Issue Type**: Off-by-one error.
**Notes**: typeof NaN returns number and reduce has no initial value. Fix with Number.isNaN and initial value 0.

## Bug 4 – bug4.js
**Intended Behavior**: The async function should fetch a JSON array of user objects and return names in uppercase.
**Issue Type**: Misuse of data types or libraries.
**Notes**: fetch and response.json return Promises but are not awaited. Fix by adding await before each call.

## Bug 5 – bug5.java
**Intended Behavior**: The function should count word frequencies in a sentence and return the most frequent word.
**Issue Type**: Runtime exception.
**Notes**: Null input and HashMap.get returning null cause NullPointerExceptions. Use null guard and getOrDefault.

## Bug 6 – bug6.py
**Intended Behavior**: The function should read student scores from a CSV, compute averages, and write results to a new CSV.
**Issue Type**: Misuse of data types or libraries.
**Notes**: CSV values are strings causing TypeError in sum. Fix by converting scores with float() and using with-blocks.