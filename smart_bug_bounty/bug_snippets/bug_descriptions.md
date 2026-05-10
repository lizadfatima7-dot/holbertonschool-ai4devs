python -c "
lines = [
    '# Bug Descriptions',
    '',
    '## bug1.py',
    '- **Intended Behavior**: The function get_last_n accepts a list and integer n and returns a new list containing only the last n elements. Given [10,20,30,40,50] and n=3 the expected output is [30,40,50].',
    '- **Current Issue**: Off-by-one error. The loop uses range(start, len(items)+1) causing IndexError on the last iteration. Fix by replacing len(items)+1 with len(items).',
    '',
    '## bug2.py',
    '- **Intended Behavior**: The function factorial accepts a non-negative integer n and returns n factorial. Given n=5 the expected output is 120. Given n=0 the expected output is 1.',
    '- **Current Issue**: Logical error. result is initialized to 0 instead of 1 making all products zero. Loop uses range(1, n) excluding n. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.',
    '',
    '## bug3.js',
    '- **Intended Behavior**: The function average accepts an array of mixed values, filters non-numeric values including NaN, and returns the arithmetic mean rounded to 2 decimal places as a number. Given [1,2,3,4,5] the expected output is 3.',
    '- **Current Issue**: typeof NaN returns number so NaN passes the filter. reduce has no initial value causing TypeError. toFixed returns a string. Fix by adding Number.isNaN check, passing 0 to reduce, and using parseFloat.',
    '',
    '## bug4.js',
    '- **Intended Behavior**: The async function getUserNames accepts a URL, fetches a JSON array of user objects, and returns each user name converted to uppercase. Given a URL returning [{name: Alice}] the expected output is [ALICE].',
    '- **Current Issue**: fetch and response.json return Promises but neither is awaited so the function maps over unresolved Promises. Fix by adding await before fetch and before response.json.',
    '',
    '## bug5.java',
    '- **Intended Behavior**: countWords accepts a sentence and returns a HashMap mapping each word to its frequency. mostFrequent returns the word with the highest count. Given the cat sat on the mat the cat the expected most frequent word is the with count 3.',
    '- **Current Issue**: Null input throws NullPointerException on split. HashMap.get returns null for unseen words causing NullPointerException on increment. Fix by adding null guard and using getOrDefault(word, 0)+1.',
    '',
    '## bug6.py',
    '- **Intended Behavior**: The function process_scores reads a CSV file where each row contains a student name followed by numeric scores, computes the average per student, and writes a new CSV with Name and Average columns. Given input row Alice,85,90,78 the expected output row is Alice,84.33.',
    '- **Current Issue**: CSV values are strings so sum raises TypeError. Files opened without with blocks cause resource leaks. Fix by converting scores with float() and using with open blocks.',
]
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\smart_bug_bounty\bug_snippets\bug_descriptions.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('Done')
"