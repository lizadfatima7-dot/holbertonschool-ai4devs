# Bug Analysis Report

This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
Each snippet contains one or more bugs covering syntax errors, logical errors, runtime exceptions, and type misuse.

---

## Bug 1 - bug1.py

Intended Behavior: The function get_last_n should accept a list and integer n, then return a new list containing only the last n elements of the original list. For example given [10, 20, 30, 40, 50] and n=3 the expected output is [30, 40, 50].

Issue Type: Off-by-one error.

Notes: The loop uses range(start, len(items)+1) which goes one index past the end of the list. On the last iteration items[i] raises IndexError because the index equals len(items). The fix is to change len(items)+1 to len(items) in the range call.

---

## Bug 2 - bug2.py

Intended Behavior: The function factorial should accept a non-negative integer n and return its factorial. For example factorial(5) should return 120 and factorial(0) should return 1.

Issue Type: Logical error.

Notes: result is initialized to 0 instead of 1 so every multiplication produces zero regardless of input. The loop uses range(1, n) which excludes n itself so the last factor is never multiplied. The base case only handles n==1 and misses n==0. Fix by setting result=1, changing range to range(1, n+1), and adding a check that returns 1 when n equals 0.

---

## Bug 3 - bug3.js

Intended Behavior: The function average should accept an array of mixed values, filter out anything that is not a valid number, compute the mean of the remaining numbers, and return it rounded to 2 decimal places as a number. For example average([1, 2, 3, 4, 5]) should return 3.00.

Issue Type: Logical error and type coercion.

Notes: In JavaScript typeof NaN equals number so NaN values pass the filter and corrupt the sum. The reduce call has no initial accumulator value which throws TypeError when the filtered array is empty. The toFixed method returns a string so arithmetic on the result fails silently. Fix by replacing the filter with a check that excludes NaN, adding 0 as the initial value for reduce, and returning parseFloat of the toFixed result.

---

## Bug 4 - bug4.js

Intended Behavior: The function getUserNames should asynchronously fetch a list of user objects from a given URL, extract the name property from each user object, convert each name to uppercase, and return the resulting array of strings.

Issue Type: Missing await in asynchronous code.

Notes: The call to fetch is missing await so response is an unresolved Promise object instead of a Response. Calling json on a Promise object throws TypeError immediately. The function call at the bottom is also not awaited so result always holds a pending Promise and the console prints Promise pending instead of names. Fix by adding await before fetch, adding await before response.json, and awaiting the function call at the bottom or using then.

---

## Bug 5 - bug5.java

Intended Behavior: The function countWords should accept a sentence string, split it into words, count occurrences of each word, and return a map of word to count. The function mostFrequent should accept that map and return the single word with the highest count. For the sentence the cat sat on the mat the cat the expected result is the with count 3.

Issue Type: Runtime NullPointerException and logical error.

Notes: The function does not check whether sentence is null before calling toLowerCase so a null input throws NullPointerException immediately. Inside the loop HashMap.get returns null for any word not yet in the map and adding 1 to null throws NullPointerException. The comparison using >= in mostFrequent causes non-deterministic results on ties because HashMap iteration order is undefined. Fix by adding a null guard at the top, replacing counts.get(word)+1 with counts.getOrDefault(word, 0)+1, and changing >= to >.

---

## Bug 6 - bug6.py

Intended Behavior: The function process_scores should read a CSV file where each row has a student name in the first column followed by numeric score values in the remaining columns, compute the average of those numeric scores for each student, and write a new CSV file with two columns named Name and Average containing each student name and their computed average.

Issue Type: Runtime TypeError and resource leak.

Notes: The csv reader returns all values as strings so scores is a list of strings not numbers. Calling sum on a list of strings raises TypeError because string addition is not numeric addition. Each value must be converted using float before summing. Both files are opened using open without a with statement so if an exception occurs the file handles are never closed causing a resource leak. The output file has no explicit close call so buffered data may never be written to disk. Fix by wrapping each score in float, opening both files using with open, and removing the manual close calls.