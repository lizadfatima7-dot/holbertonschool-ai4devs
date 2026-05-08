$content = @"
# Bug Analysis Report
This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
Each snippet contains one or more bugs covering syntax errors, logical errors, runtime exceptions, and type misuse.

---

## Bug 1 - bug1.py
**Intended Behavior**: The function get_last_n should accept a list and integer n, then return a new list containing only the last n elements of the original list. For example given [10, 20, 30, 40, 50] and n=3 the expected output is [30, 40, 50].
**Issue Type**: Off-by-one error.
**Notes**: The loop uses range(start, len(items)+1) as upper bound causing IndexError when n equals len(items). Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
**Intended Behavior**: The function factorial should accept a non-negative integer n and return its factorial. For example factorial(5) returns 120 and factorial(0) returns 1.
**Issue Type**: Logical error.
**Notes**: result is initialized to 0 instead of 1 making every multiplication produce zero. The loop uses range(1, n) which excludes n itself. Fix by setting result=1, using range(1, n+1), and adding if n == 0 return 1.

## Bug 3 - bug3.js
**Intended Behavior**: The function average should filter non-numeric values from an array and return the numeric average of valid numbers rounded to 2 decimal places. For example average([1, 2, 3, 4, 5]) returns 3.00.
**Issue Type**: Logical error and type coercion.
**Notes**: typeof NaN equals number in JavaScript so NaN passes the filter. reduce has no initial value causing TypeError on empty arrays. toFixed returns a string not a number. Fix by adding isNaN check, passing 0 to reduce, and returning parseFloat of the result.

## Bug 4 - bug4.js
**Intended Behavior**: The function getUserNames should asynchronously fetch a list of user objects from a URL and return an array of their names converted to uppercase strings.
**Issue Type**: Missing await in asynchronous code.
**Notes**: fetch is called without await so response holds an unresolved Promise. Calling json on a Promise throws TypeError. The call site does not await the function so result is always pending. Fix by adding await before fetch and before response.json and awaiting the call site.

## Bug 5 - bug5.java
**Intended Behavior**: The function countWords should count word frequencies in a sentence and mostFrequent should return the most frequent word. For the sentence the cat sat on the mat the cat the expected result is the with count 3.
**Issue Type**: Runtime NullPointerException and logical error.
**Notes**: No null check exists so passing null throws NullPointerException. HashMap.get returns null for unseen words causing NullPointerException when adding 1. Fix by adding a null guard and using getOrDefault(word, 0)+1 and changing >= to >.

## Bug 6 - bug6.py
**Intended Behavior**: The function process_scores should read a CSV file where each row contains a student name and numeric scores, compute the numeric average, and write a new CSV with columns Name and Average. For a row like Alice,80,90,100 the expected output is Alice,90.0.
**Issue Type**: Runtime TypeError and resource leak.
**Notes**: CSV values are read as strings not numbers so scores contains strings by default and calling sum raises TypeError. Each score must be converted with float before summing. Files opened without with statement cause resource leaks. Fix by converting scores with float and using with open for both files.
"@
[System.IO.File]::WriteAllText("C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_descriptions.md", $content, [System.Text.Encoding]::UTF8)