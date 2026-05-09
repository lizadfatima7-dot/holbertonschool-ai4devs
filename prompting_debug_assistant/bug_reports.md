$path = "C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_reports.md"
$content = @"
## Bug Report - bug1.py
- **Summary**: Off-by-one error in loop range causing IndexError.
- **Root Cause**: The loop uses range(start, len(items)+1) which exceeds the last valid index. On the final iteration items[len(items)] is accessed but valid indexes end at len(items)-1.
- **Resolution**: Changed len(items)+1 to len(items) in the range call. AI suggested this fix immediately. No manual edits needed.
- **Lesson Learned**: Always verify loop upper bounds. Using len(items) as the exclusive upper bound in range() is the correct pattern in Python.

## Bug Report - bug2.py
- **Summary**: Logical error causing factorial to always return 0.
- **Root Cause**: result is initialized to 0 instead of 1, so every multiplication produces 0. Additionally range(1, n) excludes n from the product and there is no base case for n equals 0.
- **Resolution**: Set result=1, changed range(1, n) to range(1, n+1), and added return 1 when n equals 0. AI identified all three issues. No manual edits needed.
- **Lesson Learned**: Multiplicative accumulators must be initialized to 1, not 0. Always test edge cases like n=0 and n=1.

## Bug Report - bug3.js
- **Summary**: Three bugs causing incorrect filtering, TypeError on empty arrays, and wrong return type.
- **Root Cause**: typeof NaN returns number so NaN passes the filter. reduce has no initial accumulator causing TypeError when array is empty. toFixed returns a string instead of a number.
- **Resolution**: Added Number.isNaN(n) to filter, passed 0 as initial value to reduce, and wrapped result with parseFloat. AI suggested all fixes. No manual edits needed.
- **Lesson Learned**: In JavaScript typeof NaN is number, so explicit NaN checks are required. Always provide an initial value to reduce to handle empty arrays safely.

## Bug Report - bug4.js
- **Summary**: Missing await causes function to operate on unresolved Promises.
- **Root Cause**: fetch and response.json both return Promises but neither is awaited. The function maps over a Promise object instead of an array, causing TypeError at runtime.
- **Resolution**: Added await before fetch(url) and await before response.json(). AI identified both missing awaits immediately. No manual edits needed.
- **Lesson Learned**: Every async function call that returns a Promise must be awaited before its result can be used. Silent failures from missing await are common and hard to debug.

## Bug Report - bug5.java
- **Summary**: NullPointerException on null input and on first occurrence of any word.
- **Root Cause**: Calling split on a null string throws NullPointerException. HashMap.get returns null for keys not yet in the map, and adding 1 to null causes NullPointerException during unboxing.
- **Resolution**: Added null check at start of countWords returning empty HashMap. Replaced counts.get(word)+1 with counts.getOrDefault(word, 0)+1. AI suggested both fixes. No manual edits needed.
- **Lesson Learned**: Always guard against null inputs in Java. Use getOrDefault instead of get when working with HashMaps to avoid NullPointerException on missing keys.

## Bug Report - bug6.py
- **Summary**: TypeError from string scores and resource leaks from unclosed files.
- **Root Cause**: csv.reader returns all values as strings so passing them directly to sum raises TypeError. Files opened without with blocks are not guaranteed to close if an exception occurs during processing.
- **Resolution**: Converted each score to float using float() before summing. Wrapped both file operations in with open blocks. AI suggested both fixes. No manual edits needed.
- **Lesson Learned**: CSV values are always strings and must be explicitly converted before arithmetic operations. Always use with open to ensure files are properly closed even when exceptions occur.
"@
[System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::ASCII)