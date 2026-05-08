@"
import io
content = (
'## Bug 1 \u2013 bug1.py\n'
'**Intended Behavior**: The function get_last_n returns a new list containing only the last n elements of the input list.  \n'
'**Issue Type**: Off-by-one error.  \n'
'**Notes**: The loop uses range(start, len(items)+1) causing IndexError when n equals len(items). Fix by replacing len(items)+1 with len(items).\n'
'\n'
'## Bug 2 \u2013 bug2.py\n'
'**Intended Behavior**: The function factorial returns the product of all positive integers from 1 to n, with factorial(0) returning 1.  \n'
'**Issue Type**: Logical error.  \n'
'**Notes**: result is initialized to 0 instead of 1 so all products are zero. Loop uses range(1, n) excluding n. Fix by setting result=1, using range(1, n+1), and returning 1 when n equals 0.\n'
'\n'
'## Bug 3 \u2013 bug3.js\n'
'**Intended Behavior**: The function average filters non-numeric values from an array and returns the arithmetic mean of the remaining numbers rounded to 2 decimal places.  \n'
'**Issue Type**: Off-by-one error.  \n'
'**Notes**: typeof NaN returns number so NaN passes the filter. reduce has no initial value causing TypeError. toFixed returns a string. Fix by adding Number.isNaN check, passing 0 to reduce, and using parseFloat.\n'
'\n'
'## Bug 4 \u2013 bug4.js\n'
'**Intended Behavior**: The async function getUserNames fetches a JSON array of user objects from a URL and returns each user name converted to uppercase.  \n'
'**Issue Type**: Misuse of data types or libraries.  \n'
'**Notes**: fetch and response.json return Promises but neither is awaited so the function maps over unresolved Promises. Fix by adding await before fetch and before response.json.\n'
'\n'
'## Bug 5 \u2013 bug5.java\n'
'**Intended Behavior**: countWords returns a HashMap mapping each word to its frequency. mostFrequent returns the word with the highest count.  \n'
'**Issue Type**: Runtime exception.  \n'
'**Notes**: Null input throws NullPointerException on split. HashMap.get returns null for unseen words causing NullPointerException on increment. Fix by adding a null guard and using getOrDefault(word, 0)+1.\n'
'\n'
'## Bug 6 \u2013 bug6.py\n'
'**Intended Behavior**: process_scores reads a CSV of student names and scores, computes each average, and writes a new CSV with Name and Average columns.  \n'
'**Issue Type**: Misuse of data types or libraries.  \n'
'**Notes**: CSV values are strings so sum raises TypeError. Files without with blocks cause resource leaks. Fix by converting scores with float() and using with open blocks.\n'
)
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompting_debug_assistant\bug_snippets\bug_descriptions.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
"@ | Out-File -FilePath "write_bugs.py" -Encoding utf8
python write_bugs.py