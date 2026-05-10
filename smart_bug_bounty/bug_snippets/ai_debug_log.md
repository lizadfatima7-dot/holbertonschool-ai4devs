# AI Debug Log

## Bug 1 – bug1.py
**AI Diagnosis**: The loop range `len(items)+1` exceeds list bounds, causing an `IndexError`.
**Suggested Fix**: Change the range to `len(items)`.
**Confidence**: High
**Result**: Fix works as expected.

## Bug 2 – bug2.py
**AI Diagnosis**: Initializing `result` to 0 makes the final factorial product 0.
**Suggested Fix**: Initialize `result = 1` and use `range(1, n + 1)`.
**Confidence**: High
**Result**: Fix works as expected.

## Bug 3 – bug3.js
**AI Diagnosis**: `NaN` is technically a "number" type in JS, and `reduce` needs an initial value for empty/mixed arrays.
**Suggested Fix**: Use `!Number.isNaN(val)` and `reduce((acc, n) => acc + n, 0)`.
**Confidence**: High
**Result**: Fix works as expected.

## Bug 4 – bug4.js
**AI Diagnosis**: The code attempts to map over a Promise object instead of the actual data because `await` is missing.
**Suggested Fix**: Use `await fetch(url)` and `await response.json()`.
**Confidence**: High
**Result**: Fix works as expected.