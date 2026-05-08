$content = @"
# Bug Analysis Report
This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.

## Bug 1 - bug1.py
Intended Behavior: The function get_last_n accepts a list and integer n and should return only the last n elements. When called with [10, 20, 30, 40, 50] and n=3 it should return [30, 40, 50] but instead raises IndexError due to an off-by-one mistake in the loop range.
Issue Type: Off-by-one error.
Notes: The loop uses range(start, len(items)+1) which exceeds the valid index range. Fix by changing len(items)+1 to len(items).

## Bug 2 - bug2.py
Intended Behavior: The function factorial accepts a non-negative integer n and should return its factorial using iteration. For example factorial(5) should return 120 and factorial(0) should return 1 but the function always returns 0 due to wrong initialization.
Issue Type: Logical error.
Notes: result is set to 0 instead of 1 so all multiplications produce zero. The loop range excludes n and the base case misses n==0. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

## Bug 3 - bug3.js
Intended Behavior: The function average accepts a mixed array and should filter out non-numeric values then return the numeric average rounded to 2 decimal places as a number. For example average([1,2,3,4,5]) should return 3.00 but crashes on empty arrays and lets NaN corrupt results.
Issue Type: Logical error and type coercion.
Notes: typeof NaN equals number so NaN passes the filter. reduce has no initial value causing TypeError on empty arrays. toFixed returns a string. Fix by filtering NaN, adding 0 as initial value, and using parseFloat.

## Bug 4 - bug4.js
Intended Behavior: The function getUserNames should asynchronously fetch user objects from a URL and return their names as uppercase strings but instead returns a pending Promise because await is missing.
Issue Type: Missing await in asynchronous code.
Notes: fetch and response.json are called without await so both return Promises. The call site also does not await the function. Fix by adding await before fetch, before response.json, and at the call site.

## Bug 5 - bug5.java
Intended Behavior: The function countWords should count word frequencies in a sentence and mostFrequent should return the most frequent word but throws NullPointerException on null input and on the first occurrence of any word.
Issue Type: Runtime NullPointerException and logical error.
Notes: No null check exists before toLowerCase. HashMap.get returns null for unseen words causing NullPointerException when adding 1. Fix by adding null guard and using getOrDefault(word, 0)+1 and changing >= to >.

## Bug 6 - bug6.py
Intended Behavior: The function process_scores should read a CSV of student scores where each value is numeric, compute each student average, and write a new CSV with Name and Average columns but raises TypeError because CSV values are strings not numbers.
Issue Type: Runtime TypeError and resource leak.
Notes: CSV parsing returns strings so sum raises TypeError. Files opened without with statement cause resource leaks. Fix by converting each score with float and using with open for both files.
"@
[System.IO.File]::WriteAllText("C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md", $content, [System.Text.Encoding]::UTF8)