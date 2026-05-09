python -c "
content = '''# Edge Case Identification Prompt Template

**Role**: QA Engineer
**Task**: Identify all edge cases and boundary conditions for the given [LANGUAGE] function that could cause unexpected behavior or failures.
**Input Placeholder**: [FUNCTION_SIGNATURE], [FUNCTION_DESCRIPTION]
**Expected Output**: A categorized list of edge cases with input values, expected outputs, and potential risk level.

---

## Example Prompt

You are a QA engineer specializing in edge case analysis.
Identify all edge cases for the following [LANGUAGE] function.

Function signature: [FUNCTION_SIGNATURE]
Description: [FUNCTION_DESCRIPTION]

For each edge case provide: input value, expected output, and risk level (low / medium / high).
Include boundary values, empty inputs, null values, and type mismatches.'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompts\edge_case_identification.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
"