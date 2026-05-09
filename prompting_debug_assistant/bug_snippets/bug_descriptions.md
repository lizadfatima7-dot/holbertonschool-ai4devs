$path = "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md"
$content = @"
## Bug 1 - bug1.py
**Intended Behavior**: The function should return a new list containing only the last n elements of the input list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses len(items)+1 as upper bound causing IndexError. Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
**Intended Behavior**: The function should return the factorial of n as the product of all integers from 1 to n, with factorial(0) returning 1.
**Issue Type**: Logical error.
**Notes**: result is initialized to 0 instead of 1 making all products zero. Loop uses range(1, n) excluding n. Fix by setting result=1 and using range(1, n+1).

## Bug 3 - bug3.js
**Intended Behavior**: The function should filter non-numeric values from an array and return the arithmetic mean of remaining numbers rounded to 2 decimal places.
**Issue Type**: Off-by-one error.
**Notes**: typeof NaN returns number so NaN passes the filter. reduce has no initial value causing TypeError. toFixed returns a string. Fix with Number.isNaN, initial value 0, and parseFloat.

## Bug 4 - bug4.js
**Intended Behavior**: The async function should fetch a JSON array of user objects from a URL and return each user name converted to uppercase.
**Issue Type**: Misuse of data types or libraries.
**Notes**: fetch and response.json return Promises but neither is awaited so the function maps over unresolved Promises. Fix by adding await before each call.

## Bug 5 - bug5.java
**Intended Behavior**: The function should count word frequencies in a sentence and return the most frequent word.
**Issue Type**: Runtime exception.
**Notes**: Null input throws NullPointerException on split. HashMap.get returns null for unseen words causing NullPointerException on increment. Fix with null guard and getOrDefault(word, 0)+1.

## Bug 6 - bug6.py
**Intended Behavior**: The function should read student names and scores from a CSV, compute each average, and write results to a new CSV with Name and Average columns.
**Issue Type**: Misuse of data types or libraries.
**Notes**: CSV values are strings so sum raises TypeError. Files without with blocks cause resource leaks. Fix by converting scores with float() and using with open blocks.
"@
[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::ASCII)