# Bug Analysis Report

This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.

## Bug 1 - bug1.py

Intended Behavior: The function get_last_n accepts a list and integer n and returns a new list containing only the last n elements of the original list.

Issue Type: Off-by-one error.

Notes: The loop uses range(start, len(items)+1) which exceeds the valid index range causing IndexError. Fix by changing len(items)+1 to len(items).

## Bug 2 - bug2.py

Intended Behavior: The function factorial accepts a non-negative integer n and returns the product of all positive integers from 1 to n. For n=0 it returns 1.

Issue Type: Logical error.

Notes: result is initialized to 0 instead of 1 making all multiplications produce zero. The loop uses range(1, n) excluding n itself. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.

## Bug 3 - bug3.js

Intended Behavior: The function average accepts an array of mixed values, filters out non-numeric entries, and returns the mean of the remaining numbers rounded to 2 decimal places as a numeric value.

Issue Type: Logical error and type coercion.

Notes: typeof NaN equals number so NaN passes the filter. reduce has no initial value causing TypeError on empty arrays. toFixed returns a string not a number. Fix by filtering NaN explicitly, passing 0 as initial value to reduce, and returning parseFloat of the result.

## Bug 4 - bug4.js

Intended Behavior: The function getUserNames accepts a URL, fetches an array of user objects from that URL, and returns a new array containing each user name converted to uppercase.

Issue Type: Missing await in asynchronous code.

Notes: fetch and response.json are called without await so both return Promises instead of resolved values. The call site does not await the async function. Fix by adding await before fetch, before response.json, and at the call site.

## Bug 5 - bug5.java

Intended Behavior: The function countWords accepts a sentence string and returns a map of each unique word to its frequency count. The function mostFrequent accepts that map and returns the word with the highest count.

Issue Type: Runtime NullPointerException and logical error.

Notes: No null check exists before calling toLowerCase so null input throws NullPointerException. HashMap.get returns null for unseen words causing NullPointerException when adding 1. Fix by adding a null guard, using getOrDefault(word, 0)+1, and changing >= to >.

## Bug 6 - bug6.py

Intended Behavior: The function process_scores accepts paths to an input and output CSV file. It reads each row which contains a student name followed by numeric score values, computes the average of those scores, and writes a new CSV with columns Name and Average.

Issue Type: Runtime TypeError and resource leak.

Notes: CSV row values are strings not numbers so calling sum raises TypeError. Files are opened without a with statement causing resource leaks if an exception occurs. Fix by converting each score with float and using with open for both files.