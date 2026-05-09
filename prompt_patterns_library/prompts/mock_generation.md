python -c "
content = '''# Mock Generation Prompt Template

**Role**: Test Engineer
**Task**: Create a mock or stub for the external dependency used in the given [LANGUAGE] function to enable isolated unit testing.
**Input Placeholder**: [FUNCTION_CODE], [DEPENDENCY_NAME]
**Expected Output**: A mock implementation of [DEPENDENCY_NAME] with configurable return values and call verification support.

---

## Example Prompt

You are a test engineer creating mock objects for unit testing.
The following [LANGUAGE] function depends on [DEPENDENCY_NAME] which cannot be used in tests.

\`\`\`
[FUNCTION_CODE]
\`\`\`

Create a mock for [DEPENDENCY_NAME] using [TEST_FRAMEWORK] that:
- Returns configurable values
- Tracks how many times it was called
- Can simulate error conditions

Include an example test that uses the mock.'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompts\mock_generation.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
"