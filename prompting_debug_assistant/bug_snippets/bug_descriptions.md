@"
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md', 'w', encoding='utf-8') as f:
    f.write("""# Bug Analysis Report
This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
---
## Bug 1 - bug1.py
- **Intended Behavior**: The function get_last_n accepts a list and integer n and returns a new list containing only the last n elements. Given [10,20,30,40,50] and n=3 the expected output is [30,40,50].
- **Issue Type**: Off-by-one error.
- **Notes**: The loop uses range(start, len(items)+1) which exceeds valid index bounds causing IndexError. Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
- **Intended Behavior**: The function factorial accepts a non-negative integer n and returns the product of all positive integers from 1 to n. Given n=5 the expected output is 120. Given n=0 the expected output is 1.
- **Issue Type**: Logical error.
- **Notes**: result is initialized to 0 instead of 1 so all multiplications produce 0. The loop uses range(1, n) which excludes n. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

## Bug 3 - bug3.js
- **Intended Behavior**: The function average accepts an array of mixed values, filters out non-numeric values including NaN, and returns the arithmetic mean rounded to 2 decimal places as a number. Given [1,2,3,4,5] the expected output is 3.
- **Issue Type**: Off-by-one error.
- **Notes**: typeof NaN returns number so NaN passes the filter. reduce has no initial value causing TypeError on empty arrays. toFixed returns a string not a number. Fix by adding Number.isNaN check, passing 0 to reduce, and wrapping with parseFloat.

## Bug 4 - bug4.js
- **Intended Behavior**: The async function getUserNames accepts a URL, fetches a JSON array of user objects, and returns each user name converted to uppercase. Given a URL returning [{name: Alice},{name: Bob}] the expected output is [ALICE, BOB].
- **Issue Type**: Misuse of data types or libraries.
- **Notes**: fetch and response.json both return Promises but neither is awaited so the function maps over unresolved Promises instead of actual data. Fix by adding await before fetch and before response.json.

## Bug 5 - bug5.java
- **Intended Behavior**: The function countWords accepts a sentence string and returns a HashMap mapping each word to its frequency count. The function mostFrequent returns the word with the highest count. Given the cat sat on the mat the cat the expected most frequent word is the with count 3.
- **Issue Type**: Runtime exception.
- **Notes**: Null input throws NullPointerException when split is called. HashMap.get returns null for unseen words causing NullPointerException on increment. Fix by adding a null guard and using getOrDefault(word, 0)+1.

## Bug 6 - bug6.py
- **Intended Behavior**: The function process_scores reads a CSV where each row has a student name and numeric scores, computes the average per student, and writes a new CSV with Name and Average columns. Given input row Alice,85,90,78 the expected output row is Alice,84.33.
- **Issue Type**: Misuse of data types or libraries.
- **Notes**: CSV values are strings so sum raises TypeError. Files without with blocks cause resource leaks. Fix by converting scores with float() and using with open blocks for both files.
""")
print('Done')
"@ | Out-File -FilePath "write_bugs.py" -Encoding utf8
python write_bugs.py