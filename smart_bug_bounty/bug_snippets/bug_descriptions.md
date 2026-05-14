# Bug Descriptions

## Bug 1 - bug1.py
- **Intended Behavior**: Return the last n items of a list.
- **Issue Type**: Off-by-one error.
- **Notes**: Loop uses len(items)+1. Fix by using len(items).

## Bug 2 - bug2.py
- **Intended Behavior**: Return the factorial of n.
- **Issue Type**: Logical error.
- **Notes**: Result initialized to 0. Set result=1 and use range(1, n+1).

## Bug 3 - bug3.js
- **Intended Behavior**: Filter non-numeric values and return mean.
- **Issue Type**: Logic error.
- **Notes**: NaN passes filter. Use Number.isNaN and initial value 0 for reduce.