$path = "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\ai_debug_log.md"
$content = @"
## Bug 1 - bug1.py
**AI Diagnosis**: The range() call uses len(items)+1 as the upper bound, which causes the loop to access items[len(items)] on the final iteration. Since valid indexes end at len(items)-1, this raises an IndexError.
**Suggested Fix**: Change len(items)+1 to len(items) in the range() call.
**Alternative Fixes Tested**: Using items[-n:] slice instead of the loop works correctly and is more Pythonic.
**Result**: Both fixes work. The slice approach is simpler.

## Bug 2 - bug2.py
**AI Diagnosis**: result is initialized to 0 instead of 1, making all multiplications produce 0. The loop uses range(1, n) which excludes n from the product. There is no base case for n equals 0.
**Suggested Fix**: Set result=1, change range(1, n) to range(1, n+1), and return 1 when n equals 0.
**Alternative Fixes Tested**: Using math.factorial(n) as a one-line alternative also works correctly.
**Result**: Both fixes work as expected.

## Bug 3 - bug3.js
**AI Diagnosis**: typeof NaN returns number so NaN values pass the numeric filter incorrectly. The reduce call has no initial accumulator value causing TypeError when the filtered array is empty. toFixed returns a string instead of a number.
**Suggested Fix**: Add Number.isNaN(n) to the filter condition, pass 0 as initial value to reduce, and wrap the result with parseFloat.
**Alternative Fixes Tested**: Using isFinite(n) instead of Number.isNaN check also filters NaN and non-numeric values correctly.
**Result**: Both fixes work correctly.

## Bug 4 - bug4.js
**AI Diagnosis**: fetch and response.json both return Promises but neither is awaited. The function attempts to map over an unresolved Promise object instead of an array, causing a TypeError at runtime.
**Suggested Fix**: Add await before fetch(url) and add await before response.json().
**Alternative Fixes Tested**: Using .then() chaining instead of async/await also resolves the Promises correctly.
**Result**: Both async/await and .then() approaches work correctly.

## Bug 5 - bug5.java
**AI Diagnosis**: Passing null throws NullPointerException when split is called on the null reference. For unseen words, HashMap.get returns null and incrementing null causes NullPointerException during unboxing.
**Suggested Fix**: Add a null check at the start of countWords that returns an empty HashMap, and replace counts.get(word)+1 with counts.getOrDefault(word, 0)+1.
**Alternative Fixes Tested**: Using a ConcurrentHashMap with merge method also avoids the null issue cleanly.
**Result**: Both fixes work as expected.

## Bug 6 - bug6.py
**AI Diagnosis**: CSV values are read as strings so passing them directly to sum raises TypeError. Files are opened without with statements causing resource leaks if an exception occurs during processing.
**Suggested Fix**: Convert each score to float using float() before summing and wrap all file operations in with open blocks.
**Alternative Fixes Tested**: Using pandas read_csv and to_csv handles type conversion and file closing automatically.
**Result**: Both fixes work. The with open approach is more lightweight.
"@
[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::ASCII)