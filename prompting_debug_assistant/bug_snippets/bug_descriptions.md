$content = @"
## Bug 1 - bug1.py
**Intended Behavior**: The function get_last_n accepts a list and integer n and returns a new list containing only the last n elements. Example: get_last_n([1,2,3,4,5], 3) should return [3,4,5].
**Issue Type**: Off-by-one error.
**Notes**: The loop iterates with range(start, len(items)+1) which exceeds valid index bounds and causes an IndexError on the last iteration. Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
**Intended Behavior**: The function factorial accepts a non-negative integer n and returns n!. Example: factorial(5) should return 120, factorial(0) should return 1.
**Issue Type**: Logical error.
**Notes**: result is initialized to 0 instead of 1, making all products zero. The loop uses range(1, n) which excludes n itself. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

## Bug 3 - bug3.js
**Intended Behavior**: The function average accepts an array of mixed values, filters out non-numeric values, and returns the arithmetic mean of remaining numbers rounded to 2 decimal places as a number. Example: average([1, "a", 2, NaN, 3]) should return 2.00.
**Issue Type**: Off-by-one error.
**Notes**: typeof NaN returns "number" so NaN passes the filter. reduce has no initial accumulator causing TypeError on empty arrays. toFixed returns a string not a number. Fix by adding Number.isNaN check, passing 0 as initial value to reduce, and wrapping result with parseFloat.

## Bug 4 - bug4.js
**Intended Behavior**: The async function getUserNames accepts a URL string, fetches a JSON array of user objects from that URL, and returns an array of each user's name in uppercase. Example: getUserNames(url) should return ["ALICE", "BOB"].
**Issue Type**: Misuse of data types or libraries.
**Notes**: fetch and response.json both return Promises but neither is awaited, so the function maps over an unresolved Promise instead of the actual data array. Fix by adding await before fetch and before response.json.

## Bug 5 - bug5.java
**Intended Behavior**: countWords accepts a sentence string and returns a HashMap of each word mapped to its frequency count. mostFrequent iterates the map and returns the word with the highest count. Example: countWords("hello world hello") should return {hello=2, world=1}.
**Issue Type**: Runtime exception.
**Notes**: Passing null throws NullPointerException when split is called. HashMap.get returns null for unseen words causing NullPointerException during unboxing on increment. Fix by adding a null guard at the start of countWords and using getOrDefault(word, 0)+1 instead of get.

## Bug 6 - bug6.py
**Intended Behavior**: The function process_scores reads a CSV file where each row has a student name followed by numeric scores, computes the average per student, and writes a new CSV with Name and Average columns. Example input row: Alice,85,90,78. Example output row: Alice,84.33.
**Issue Type**: Misuse of data types or libraries.
**Notes**: CSV values are read as strings so passing them directly to sum raises TypeError. Files are opened without with blocks causing resource leaks if an exception occurs mid-processing. Fix by converting each score value with float() before summing and wrapping all file operations in with open blocks.
"@
[System.IO.File]::WriteAllText(
  "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md",
  $content,
  [System.Text.Encoding]::UTF8
)