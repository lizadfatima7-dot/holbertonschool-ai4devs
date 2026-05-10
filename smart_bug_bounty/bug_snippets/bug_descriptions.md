# Bug Descriptions

## bug1.py
- **Intended Behavior**: The function get_last_n accepts a list and integer n and returns a new list containing only the last n elements.
- **Current Issue**: Off-by-one error. The loop uses range(start, len(items)+1) causing IndexError when accessing items[len(items)].

## bug2.py
- **Intended Behavior**: The function factorial accepts a non-negative integer n and returns the product of all positive integers from 1 to n.
- **Current Issue**: Logical error. result is initialized to 0 instead of 1. Loop uses range(1, n) excluding n. No base case for n equals 0.

## bug3.js
- **Intended Behavior**: The function average accepts an array, filters non-numeric values, and returns the arithmetic mean rounded to 2 decimal places as a number.
- **Current Issue**: typeof NaN returns number so NaN passes filter. reduce has no initial value causing TypeError. toFixed returns a string not a number.

## bug4.js
- **Intended Behavior**: The async function getUserNames accepts a URL, fetches an array of user objects, and returns each user name converted to uppercase.
- **Current Issue**: fetch and response.json are not awaited so both return Promises instead of resolved values.

## bug5.java
- **Intended Behavior**: countWords accepts a sentence and returns a HashMap of word frequencies. mostFrequent returns the word with highest count.
- **Current Issue**: Null input throws NullPointerException. HashMap.get returns null for unseen words causing NullPointerException on increment.

## bug6.py
- **Intended Behavior**: process_scores reads a CSV of student names and scores, computes each average, and writes results to a new CSV with Name and Average columns.
- **Current Issue**: CSV values are strings so sum raises TypeError. Files opened without with blocks cause resource leaks.
## bug6.py
- **Intended Behavior**: The function process_scores reads a CSV file where each row contains a student name followed by numeric scores, computes the average score per student, and writes the results to a new CSV file with Name and Average columns.
- **Current Issue**: CSV values are read as strings so passing them to sum raises TypeError. Files are opened without with blocks causing resource leaks if an exception occurs.