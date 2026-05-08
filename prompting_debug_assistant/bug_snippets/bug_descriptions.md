$content = @"
## Bug 1 – bug1.py
**Intended Behavior**: The function get_last_n accepts a list and integer n and returns a new list containing only the last n elements.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses range(start, len(items)+1) exceeding the valid index range. Fix by changing len(items)+1 to len(items).

## Bug 2 – bug2.py
**Intended Behavior**: The function factorial accepts a non-negative integer n and returns the product of all positive integers from 1 to n.
**Issue Type**: Logical error.
**Notes**: result is initialized to 0 instead of 1. The loop uses range(1, n) excluding n. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

## Bug 3 – bug3.js
**Intended Behavior**: The function average accepts an array, filters non-numeric values, and returns the mean of remaining numbers rounded to 2 decimal places.
**Issue Type**: Off-by-one error.
**Notes**: typeof NaN equals number so NaN passes the filter. reduce has no initial value causing TypeError. toFixed returns a string. Fix by filtering NaN, passing 0 to reduce, and using parseFloat.

## Bug 4 – bug4.js
**Intended Behavior**: The function getUserNames accepts a URL, fetches an array of user objects, and returns each user name converted to uppercase.
**Issue Type**: Misuse of data types or libraries.
**Notes**: fetch and response.json are missing await so both return Promises. Fix by adding await before each and awaiting the call site.

## Bug 5 – bug5.java
**Intended Behavior**: The function countWords accepts a sentence and returns a map of each word to its frequency. The function mostFrequent returns the word with the highest count.
**Issue Type**: Runtime exception.
**Notes**: Null input throws NullPointerException. HashMap.get returns null for unseen words. Fix by adding null guard and using getOrDefault(word, 0)+1.

## Bug 6 – bug6.py
**Intended Behavior**: The function process_scores reads a CSV where each row has a student name and numeric scores, computes the average, and writes a new CSV with Name and Average columns.
**Issue Type**: Misuse of data types or libraries.
**Notes**: CSV values are strings so sum raises TypeError. Files opened without with cause resource leaks. Fix by converting scores with float and using with open.
"@
[System.IO.File]::WriteAllText("C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md", $content, [System.Text.Encoding]::UTF8)