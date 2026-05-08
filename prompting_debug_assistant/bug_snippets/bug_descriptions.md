@"
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md', 'w', encoding='utf-8') as f:
    f.write("""# Bug Analysis Report
This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
Each snippet contains one or more bugs covering off-by-one errors, logical errors, runtime exceptions, and type misuse.
---
## Bug 1 - bug1.py
**Intended Behavior**: The function get_last_n should accept a list and integer n, then return a new list containing only the last n elements. Given [10,20,30,40,50] and n=3, the expected output is [30,40,50].
**Issue Type**: Off-by-one error.
**Notes**: The loop uses range(start, len(items)+1) causing IndexError when accessing items[len(items)]. Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
**Intended Behavior**: The function factorial should accept a non-negative integer n and return the product of all positive integers from 1 to n. Given n=5, the expected output is 120. Given n=0, the expected output is 1.
**Issue Type**: Logical error.
**Notes**: result is initialized to 0 instead of 1 causing all products to be zero. The loop uses range(1, n) which excludes n. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

## Bug 3 - bug3.js
**Intended Behavior**: The function average should accept an array of mixed values, filter out non-numeric values including NaN, and return the arithmetic mean of the remaining numbers rounded to 2 decimal places as a number. Given [1,2,3,4,5], the expected output is 3.
**Issue Type**: Off-by-one error.
**Notes**: typeof NaN returns number so NaN passes the filter. reduce has no initial accumulator causing TypeError. toFixed returns a string. Fix by adding Number.isNaN check, passing 0 to reduce, and wrapping with parseFloat.

## Bug 4 - bug4.js
**Intended Behavior**: The async function getUserNames should accept a URL string, fetch a JSON array of user objects, and return a new array of each user name converted to uppercase. Given a URL returning [{name: Alice}], the expected output is [ALICE].
**Issue Type**: Misuse of data types or libraries.
**Notes**: fetch and response.json both return Promises but neither is awaited so the function maps over unresolved Promises. Fix by adding await before fetch and before response.json.

## Bug 5 - bug5.java
**Intended Behavior**: The function countWords should accept a sentence string and return a HashMap where each key is a word and each value is its frequency count. The function mostFrequent should return the word with the highest count. Given the cat sat on the mat the cat, the expected most frequent word is the.
**Issue Type**: Runtime exception.
**Notes**: Null input throws NullPointerException when split is called. HashMap.get returns null for unseen words causing NullPointerException on increment. Fix by adding a null guard and using getOrDefault(word, 0)+1.

## Bug 6 - bug6.py
**Intended Behavior**: The function process_scores should read a CSV file where each row contains a student name followed by numeric scores, compute the average per student, and write results to a new CSV with Name and Average columns. Given input row Alice,85,90,78, the expected output row is Alice,84.33.
**Issue Type**: Misuse of data types or libraries.
**Notes**: CSV values are read as strings so passing them to sum raises TypeError. Files opened without with blocks cause resource leaks. Fix by converting each score with float() and using with open blocks for both files.
""")
print('Done')
"@ | Out-File -FilePath "write_bugs.py" -Encoding utf8
python write_bugs.py