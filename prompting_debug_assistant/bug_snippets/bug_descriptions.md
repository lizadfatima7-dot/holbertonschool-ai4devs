$content = @"
# Bug Analysis Report

This document describes 6 intentionally buggy code snippets across Python, JavaScript, and Java.
Each snippet contains one or more bugs covering syntax errors, logical errors, runtime exceptions, and type misuse.

---

## Bug 1 - bug1.py

**Intended Behavior**: The function ``get_last_n`` should accept a list and integer ``n``, then return a new list containing only the last ``n`` elements of the original list.

**Issue Type**: Off-by-one error.

**Notes**: The loop uses ``len(items)+1`` as upper bound causing ``IndexError`` when ``n`` equals ``len(items)``. Fix by replacing ``len(items)+1`` with ``len(items)``.

---

## Bug 2 - bug2.py

**Intended Behavior**: The function ``factorial`` should compute the factorial of a non-negative integer using an iterative approach. For ``n=5`` it should return ``120``. For ``n=0`` it should return ``1``.

**Issue Type**: Logical error (incorrect initialization).

**Notes**: ``result`` is initialized to ``0`` instead of ``1``, which causes multiplication to always produce ``0``. Additionally, ``range(1, n)`` excludes ``n`` itself and the base case for ``n=0`` is missing. Fix by setting ``result=1``, using ``range(1, n+1)``, and adding a base case for ``n=0``.

---

## Bug 3 - bug3.js

**Intended Behavior**: The function ``average`` should compute the mean of all numeric values in an array while safely ignoring non-numeric entries such as strings and ``null``. For ``[10, "hello", null, 20]`` it should return ``"15.00"``. An empty or fully invalid array should be handled without throwing.

**Issue Type**: Type filtering error and runtime exception.

**Notes**: ``reduce`` is called without an initial value, which causes a ``TypeError`` on an empty array. When ``valid`` is empty, ``0 / 0`` produces ``NaN`` instead of a safe fallback. Fix by passing ``0`` as the initial accumulator to ``reduce`` and returning ``"0.00"`` when ``valid.length === 0``.

---

## Bug 4 - bug4.js

**Intended Behavior**: The function ``getUserNames`` should asynchronously fetch a list of user objects from a given URL and return an array of each user's name converted to uppercase. For example: ``["LEANNE GRAHAM", "ERVIN HOWELL", ...]``.

**Issue Type**: Missing ``await`` in asynchronous code.

**Notes**: ``fetch(url)`` and ``response.json()`` are both called without ``await``, so ``response`` and ``data`` hold unresolved ``Promise`` objects rather than actual values. Calling ``.map()`` on a ``Promise`` throws a ``TypeError``. The function is also called synchronously outside without ``.then()``, so a ``Promise`` is logged instead of the names. Fix by adding ``await`` before both calls and using ``.then()`` at the call site.

---

## Bug 5 - bug5.java

**Intended Behavior**: The static method ``countWords`` in ``WordCounter`` should count how many times each word appears in a sentence and return a ``Map<String, Integer>``. The method ``mostFrequent`` should return the most frequently occurring word. For ``"the cat sat on the mat the cat"`` the result should be ``"the"``.

**Issue Type**: NullPointerException and logic error.

**Notes**: ``counts.get(word)`` returns ``null`` on first occurrence of any word, so ``counts.get(word) + 1`` throws a ``NullPointerException``. Additionally, ``mostFrequent`` uses ``>= max`` instead of ``> max``, which can incorrectly overwrite the best word with a later equal-frequency word. Passing ``null`` to ``countWords`` causes a ``NullPointerException`` on ``.toLowerCase()``. Fix by using ``counts.getOrDefault(word, 0) + 1``, changing ``>= max`` to ``> max``, and adding a null check at the start of ``countWords``.

---

## Bug 6 - bug6.py

**Intended Behavior**: The function ``process_scores`` should read a CSV file where each row contains a student name followed by numeric scores, compute the average score per student, and write the results to an output CSV file with columns ``Name`` and ``Average``.

**Issue Type**: Type error and resource leak.

**Notes**: ``scores`` contains raw strings from ``csv.reader``, so ``sum(scores)`` raises a ``TypeError`` because strings cannot be summed directly. The files are opened without a ``with`` statement, so if an exception occurs the file handles are never closed. Fix by converting each score with ``float()`` before summing, and wrapping both file operations in ``with`` blocks.
"@
[System.IO.File]::WriteAllText("D:\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md", $content, [System.Text.Encoding]::UTF8)