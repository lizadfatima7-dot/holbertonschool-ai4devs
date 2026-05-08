$content = @"
## Bug 1 - bug1.py
**Intended Behavior**: The function get_last_n accepts a list and integer n and returns a new list containing only the last n elements of the input list.
**Issue Type**: Off-by-one error.
**Notes**: The loop iterates using range(start, len(items)+1) which exceeds the valid index range and causes an IndexError. The correct fix is to change len(items)+1 to len(items) so the loop stops before the out-of-bounds index.

## Bug 2 - bug2.py
**Intended Behavior**: The function factorial accepts a non-negative integer n and returns the product of all positive integers from 1 to n, with factorial(0) returning 1.
**Issue Type**: Logical error.
**Notes**: result is initialized to 0 instead of 1, causing all multiplications to produce 0. The loop uses range(1, n) which excludes n from the product. Fix by setting result=1, changing range to range(1, n+1), and explicitly returning 1 when n equals 0.

## Bug 3 - bug3.js
**Intended Behavior**: The function average accepts an array, filters out non-numeric values, and returns the arithmetic mean of the remaining numbers rounded to 2 decimal places as a number.
**Issue Type**: Off-by-one error.
**Notes**: typeof NaN returns number so NaN values pass the numeric filter incorrectly. The reduce call has no initial accumulator value causing TypeError on empty arrays. toFixed returns a string instead of a number. Fix by adding Number.isNaN check to filter, passing 0 as initial value to reduce, and wrapping toFixed result with parseFloat.

## Bug 4 - bug4.js
**Intended Behavior**: The function getUserNames accepts a URL, fetches an array of user objects from that URL, and returns a new array containing each user's name converted to uppercase.
**Issue Type**: Misuse of data types or libraries.
**Notes**: fetch returns a Promise and response.json also returns a Promise, but neither is awaited. This causes the function to operate on unresolved Promise objects instead of actual data. Fix by adding await before fetch and before response.json, and ensuring the call site also awaits getUserNames.

## Bug 5 - bug5.java
**Intended Behavior**: The function countWords accepts a sentence string and returns a HashMap mapping each word to its frequency count. The function mostFrequent iterates the map and returns the word with the highest count.
**Issue Type**: Runtime exception.
**Notes**: Passing a null sentence causes NullPointerException when split is called. HashMap.get returns null for words not yet in the map, so the first occurrence causes a NullPointerException during unboxing. Fix by adding a null check at the start of countWords and replacing get with getOrDefault(word, 0)+1 to safely initialize counts.

## Bug 6 - bug6.py
**Intended Behavior**: The function process_scores reads a CSV file where each row contains a student name followed by numeric scores, computes the average score per student, and writes the results to a new CSV file with Name and Average columns.
**Issue Type**: Misuse of data types or libraries.
**Notes**: CSV values are read as strings so passing them to sum raises TypeError. Input and output files are opened without a with statement causing resource leaks if an exception occurs. Fix by converting each score value with float before summing and wrapping all file operations in with open blocks to ensure proper resource cleanup.
"@
[System.IO.File]::WriteAllText(
  "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md",
  $content,
  [System.Text.Encoding]::UTF8
)