python -c "
content = '''# Style Enforcement Prompt Template

**Role**: Code Quality Engineer
**Task**: Rewrite the given [LANGUAGE] code to follow [STYLE_GUIDE] conventions consistently.
**Input Placeholder**: [CODE_BLOCK]
**Expected Output**: Reformatted code with consistent naming, spacing, and structure. List of style violations fixed.

---

## Example Prompt

You are a code quality engineer enforcing [STYLE_GUIDE] standards.
Review the following [LANGUAGE] code and rewrite it to comply with the style guide.
Fix all naming, formatting, and structural violations.

\`\`\`
[CODE_BLOCK]
\`\`\`

Return the corrected code and a bullet list of all style issues that were fixed.'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompts\style_enforcement.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
"