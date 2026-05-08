@"
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md', 'w', encoding='utf-8') as f:
    f.write("""# Bug Analysis Report
This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
Each snippet contains one or more bugs covering off-by-one errors, logical errors, runtime exceptions, and type misuse.
---
## Bug 1 - bug1.py
### Intended Behavior
The function get_last_n accepts a list and integer n and returns a new list containing only the last n elements. Given [10,20,30,40,50] and n=3, the expected output is [30,40,50].
### Issue Type
Off-by-one error.
### Notes
The loop uses range(start, len(items)+1) which exceeds valid index bounds and causes IndexError on the last iteration. Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
### Intended Behavior
The function factorial accepts a non-negative integer n and returns the product of all positive integers from 1 to n. Given n=5 the expected output is 120. Given n=0 the expected output is 1.
### Issue Type
Logical error.
### Notes
result is initialized to 0 instead of 1 so all multiplications produce 0. The loop uses range(1, n) which excludes n from the product. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

## Bug 3 - bug3.js
### Intended Behavior
The function average accepts an array of mixed values, filters out non-numeric values including NaN, and returns the arithmetic mean of the remaining numbers rounded to 2 decimal places as a number. Given [1,2,3,4,5] the expected output is 3.
### Issue Type
Off-by-one error.
### Notes
typeof NaN returns number so NaN values pass the filter incorrectly. reduce has no initial accumulator value causing TypeError on empty arrays. toFixed returns a string instead of a number. Fix by adding Number.isNaN check to the filter, passing 0 as initial value to reduce, and wrapping the result with parseFloat.

## Bug 4 - bug4.js
### Intended Behavior
The async function getUserNames accepts a URL string, sends an HTTP request to fetch a JSON array of user objects, and returns a new array containing each user name converted to uppercase. Given a URL returning [{name: Alice},{name: Bob}] the expected output is [ALICE, BOB].
### Issue Type
Misuse of data types or libraries.
### Notes
fetch returns a Promise and response.json also returns a Promise but neither is awaited. As a result the function attempts to map over an unresolved Promise object instead of an array, producing incorrect output. Fix by adding await before fetch and before response.json.

## Bug 5 - bug5.java
### Intended Behavior
The function countWords accepts a sentence string and returns a HashMap where each key is a word and each value is its frequency count. The function mostFrequent iterates the map and returns the word with the highest count. Given the cat sat on the mat the cat the expected most frequent word is the with count 3.
### Issue Type
Runtime exception.
### Notes
Passing null as the sentence causes NullPointerException when split is called. For unseen words HashMap.get returns null and incrementing null causes NullPointerException during unboxing. Fix by adding a null check at the start of countWords and replacing get with getOrDefault(word, 0)+1.

## Bug 6 - bug6.py
### Intended Behavior
The function process_scores reads a CSV file where each row contains a student name followed by numeric scores, computes the average score per student, and writes the results to a new CSV file with Name and Average as column headers. Given input row Alice,85,90,78 the expected output row is Alice,84.33.
### Issue Type
Misuse of data types or libraries.
### Notes
CSV values are read as strings so passing them directly to sum raises TypeError. Opening files without with blocks causes resource leaks if an exception occurs during processing. Fix by converting each score value with float() before summing and wrapping all file operations in with open blocks.
""")
print('Done')
"@ | Out-File -FilePath "write_bugs.py" -Encoding utf8
python write_bugs.py