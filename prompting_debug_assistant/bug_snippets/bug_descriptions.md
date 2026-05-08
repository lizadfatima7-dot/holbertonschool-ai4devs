$content = @"
# Bug Analysis Report
This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.

## Bug 1 – bug1.py
**Intended Behavior**: The function get_last_n should accept a list and integer n, then return a new list containing only the last n elements of the original list.
**Issue Type**: Off-by-one error.
**Notes**: The loop uses range(start, len(items)+1) causing IndexError when n equals len(items). Fix by replacing len(items)+1 with len(items).

## Bug 2 – bug2.py
**Intended Behavior**: The function factorial should accept a non-negative integer n and return its factorial value.
**Issue Type**: Logical error.
**Notes**: result is initialized to 0 instead of 1. The loop range excludes n. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

## Bug 3 – bug3.js
**Intended Behavior**: The function average should filter non-numeric values and return the numeric average rounded to 2 decimal places.
**Issue Type**: Logical error and type coercion.
**Notes**: NaN passes the typeof check. reduce crashes on empty array. toFixed returns string. Fix by filtering NaN, adding initial value 0, and using parseFloat.

## Bug 4 – bug4.js
**Intended Behavior**: The function getUserNames should asynchronously fetch user objects and return their names as uppercase strings.
**Issue Type**: Missing await in asynchronous code.
**Notes**: fetch and json are called without await returning Promises instead of values. Fix by adding await before both calls and at the call site.

## Bug 5 – bug5.java
**Intended Behavior**: The function countWords should count word frequencies and mostFrequent should return the most frequent word.
**Issue Type**: Runtime NullPointerException and logical error.
**Notes**: Null input throws NullPointerException. HashMap.get returns null for new words. Fix by adding null guard and using getOrDefault(word, 0)+1.

## Bug 6 – bug6.py
**Intended Behavior**: The function process_scores should read a CSV of student scores, compute numeric averages, and write results to a new CSV file.
**Issue Type**: Runtime TypeError and resource leak.
**Notes**: CSV values are strings so sum raises TypeError. Files are not closed properly. Fix by converting scores with float and using with open for both files.
"@
[System.IO.File]::WriteAllText("C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md", $content, [System.Text.Encoding]::UTF8)