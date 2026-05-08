## Bug 1 – bug1.py
**Intended Behavior**: Return the last n items of a list.  
**Issue Type**: Off-by-one error.  
**Notes**: The function fails when n equals len(items) because range(start, len(items)+1) exceeds valid index bounds. Fix by replacing len(items)+1 with len(items).

## Bug 2 – bug2.py
**Intended Behavior**: Return the factorial of n as the product of all integers from 1 to n, with factorial(0) returning 1.  
**Issue Type**: Logical error.  
**Notes**: result initialized to 0 makes all products zero. Loop range(1, n) excludes n. Fix by setting result=1, using range(1, n+1), returning 1 when n is 0.

## Bug 3 – bug3.js
**Intended Behavior**: Filter non-numeric values from an array and return the arithmetic mean rounded to 2 decimal places as a number.  
**Issue Type**: Off-by-one error.  
**Notes**: typeof NaN returns number so NaN passes filter. reduce has no initial value causing TypeError. toFixed returns string. Fix with Number.isNaN, initial value 0, and parseFloat.

## Bug 4 – bug4.js
**Intended Behavior**: Fetch a JSON array of user objects from a URL and return each user name in uppercase.  
**Issue Type**: Misuse of data types or libraries.  
**Notes**: fetch and response.json return Promises but neither is awaited. Fix by adding await before fetch and before response.json.

## Bug 5 – bug5.java
**Intended Behavior**: Count word frequencies in a sentence and return the most frequent word.  
**Issue Type**: Runtime exception.  
**Notes**: Null input throws NullPointerException. HashMap.get returns null for unseen words causing NullPointerException on increment. Fix with null guard and getOrDefault(word, 0)+1.

## Bug 6 – bug6.py
**Intended Behavior**: Read a CSV of student scores, compute each average, and write results to a new CSV with Name and Average columns.  
**Issue Type**: Misuse of data types or libraries.  
**Notes**: CSV values are strings so sum raises TypeError. Files without with blocks cause resource leaks. Fix with float() conversion and with open blocks.