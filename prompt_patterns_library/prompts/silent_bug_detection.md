python -c "
content = '''# Silent Bug Detection Prompt Template

**Role**: QA Engineer
**Task**: Identify why the given [LANGUAGE] function produces incorrect output without throwing any errors.
**Input Placeholder**: [CODE_BLOCK], [ACTUAL_OUTPUT], [EXPECTED_OUTPUT]
**Expected Output**: Root cause of the wrong result, corrected code, and explanation of the logical error.

---

## Example Prompt

You are a QA engineer analyzing a silent bug.
The following [LANGUAGE] function runs without errors but produces wrong output.

Code:
\`\`\`
[CODE_BLOCK]
\`\`\`

Expected output: [EXPECTED_OUTPUT]
Actual output: [ACTUAL_OUTPUT]

Identify the logical error, explain why the output is wrong, and provide the corrected version.'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompts\silent_bug_detection.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
"