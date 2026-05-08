# Bug Descriptions

A collection of intentionally flawed code snippets for debugging practice.
Each snippet has a clearly defined **intended behavior**, **bug type**, and **notes** explaining what goes wrong.

---

## Bug 1 – `bug1.py`

**Language**: Python  
**Intended Behavior**: Return the last `n` items of a list using a manual index loop.  
**Issue Type**: Off-by-one error — Runtime `IndexError`  
**Notes**:  
The loop uses `range(start, len(items) + 1)` instead of `range(start, len(items))`.  
The extra `+1` pushes the index one past the end of the list on the final iteration, causing an `IndexError`.  
The bug is most visible when `n == len(items)` (i.e., asking for all elements).

---

## Bug 2 – `bug2.py`

**Language**: Python  
**Intended Behavior**: Compute the factorial of a non-negative integer (`n!`).  
**Issue Type**: Logical error — wrong base case, wrong initial value, wrong loop range  
**Notes**:  
Three compounding mistakes exist:
1. The base case only handles `n == 1`, so `factorial(0)` enters the loop and returns `0` instead of `1`.  
2. `result` is initialized to `0` instead of `1`, so every multiplication produces `0`.  
3. The loop runs `range(1, n)` instead of `range(1, n+1)`, so the value of `n` itself is never multiplied in.  
Running `factorial(5)` returns `0` instead of `120`.

---

## Bug 3 – `bug3.js`

**Language**: JavaScript  
**Intended Behavior**: Accept a mixed array, filter out non-numbers, and return the average rounded to 2 decimal places.  
**Issue Type**: Data type misuse + Runtime exception  
**Notes**:  
1. `typeof NaN === "number"` is `true` in JavaScript, so `NaN` values pass the filter and corrupt the sum.  
2. `reduce` is called without an initial accumulator value — if `valid` is empty, it throws `TypeError: Reduce of empty array with no initial value`.  
3. `toFixed()` returns a **string**, so any downstream arithmetic on the result silently fails or concatenates instead of adds.

---

## Bug 4 – `bug4.js`

**Language**: JavaScript  
**Intended Behavior**: Fetch a list of users from a REST API and return their names in uppercase.  
**Issue Type**: Misuse of `async/await` — unresolved Promises treated as values  
**Notes**:  
1. `fetch(url)` is called without `await`, so `response` holds a `Promise` object, not an actual HTTP `Response`.  
2. Calling `.json()` on a `Promise` throws a `TypeError`.  
3. The top-level call does not `await` the async function either, so `result` is always `Promise { <pending> }`.  
The snippet is useful for understanding the async execution model and why every `await`-able call must be awaited.

---

## Bug 5 – `bug5.java`

**Language**: Java  
**Intended Behavior**: Count word frequencies in a sentence, then report the most frequent word.  
**Issue Type**: Runtime `NullPointerException` + logical error in max-finding  
**Notes**:  
1. `sentence.toLowerCase()` throws `NullPointerException` when `sentence` is `null` — no guard exists.  
2. Inside the loop, `counts.get(word)` returns `null` for unseen words; adding `1` to `null` throws `NullPointerException`. The fix is `counts.getOrDefault(word, 0) + 1`.  
3. The `>=` comparison in `mostFrequent` means ties are broken by whichever entry appears last during map iteration — order in a `HashMap` is undefined, making the result non-deterministic.  
4. If `counts` is empty, `mostFrequent` returns `null` without any warning.

---

## Bug 6 – `bug6.py`

**Language**: Python  
**Intended Behavior**: Read a student scores CSV, compute each student's numeric average, and write results to a new CSV file.  
**Issue Type**: Runtime `TypeError` + library misuse + resource leak  
**Notes**:  
1. `scores` is a list of **strings** (`['85', '90', '78']`). Calling `sum()` on strings raises `TypeError: unsupported operand type(s) for +: 'int' and 'str'`. Each score must be converted with `int()` or `float()` first.  
2. Both `infile` and `outfile` are opened without a `with` statement. If an exception occurs, the files are never closed, leaking file handles.  
3. On Windows, opening the output file without `newline=""` causes the `csv` writer to insert an extra blank line between every row.  
4. The output file is never explicitly closed, so buffered data may not be flushed to disk before the program exits.
