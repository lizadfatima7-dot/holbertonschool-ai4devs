python -c "
content = '''# Unit Test Generation Prompt Template

**Role**: QA Engineer
**Task**: Generate comprehensive unit tests for the given [LANGUAGE] function covering normal cases, edge cases, and error cases.
**Input Placeholder**: [FUNCTION_CODE]
**Expected Output**: A complete test file using [TEST_FRAMEWORK] with descriptive test names and assertions for all cases.

---

## Example Prompt

You are a QA engineer writing unit tests.
Generate comprehensive unit tests for the following [LANGUAGE] function using [TEST_FRAMEWORK].

\`\`\`
[FUNCTION_CODE]
\`\`\`

Cover: normal input cases, boundary values, edge cases, and invalid input handling.
Use descriptive test names and include assertions with clear failure messages.'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompts\unit_test_generation.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
"