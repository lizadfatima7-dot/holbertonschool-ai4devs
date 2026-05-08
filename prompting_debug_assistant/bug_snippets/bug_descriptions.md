$content = @"
## Bug 1 - bug1.py
Intended Behavior: The function get_last_n accepts a list and integer n and returns a new list containing only the last n elements. Example: get_last_n([1,2,3,4,5], 3) returns [3,4,5].
Issue Type: Off-by-one error.
Notes: The loop iterates with range(start, len(items)+1) which exceeds valid index bounds. Fix by replacing len(items)+1 with len(items).

## Bug 2 - bug2.py
Intended Behavior: The function factorial accepts a non-negative integer n and returns n factorial. Example: factorial(5) returns 120, factorial(0) returns 1.
Issue Type: Logical error.
Notes: result is initialized to 0 instead of 1 making all products zero. The loop uses range(1, n) which excludes n. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

## Bug 3 - bug3.js
Intended Behavior: The function average accepts an array, filters non-numeric values, and returns the arithmetic mean rounded to 2 decimal places as a number. Example: average([1, "a", 2, NaN, 3]) returns 2.
Issue Type: Off-by-one error.
Notes: typeof NaN returns number so NaN passes the filter. reduce has no initial value causing TypeError. toFixed returns a string. Fix by adding Number.isNaN check, passing 0 to reduce, and wrapping result with parseFloat.

## Bug 4 - bug4.js
Intended Behavior: The async function getUserNames accepts a URL, fetches a JSON array of user objects, and returns each user name in uppercase. Example: getUserNames(url) returns ["ALICE", "BOB"].
Issue Type: Misuse of data types or libraries.
Notes: fetch and response.json both return Promises but neither is awaited so the function operates on unresolved Promises. Fix by adding await before fetch and before response.json.

## Bug 5 - bug5.java
Intended Behavior: countWords accepts a sentence and returns a HashMap of each word mapped to its frequency. mostFrequent returns the word with the highest count. Example: countWords("hello world hello") returns {hello=2, world=1}.
Issue Type: Runtime exception.
Notes: Null input throws NullPointerException when split is called. HashMap.get returns null for unseen words causing NullPointerException on increment. Fix by adding a null guard and using getOrDefault(word, 0)+1.

## Bug 6 - bug6.py
Intended Behavior: process_scores reads a CSV where each row has a student name and numeric scores, computes the average per student, and writes a new CSV with Name and Average columns. Example input: Alice,85,90,78. Example output: Alice,84.33.
Issue Type: Misuse of data types or libraries.
Notes: CSV values are strings so sum raises TypeError. Files opened without with blocks cause resource leaks. Fix by converting scores with float() and using with open blocks.
"@
[System.IO.File]::WriteAllText(
  "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md",
  $content,
  [System.Text.Encoding]::UTF8
)