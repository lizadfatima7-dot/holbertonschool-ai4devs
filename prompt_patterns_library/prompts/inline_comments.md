python -c "
content = '''# Inline Comment Writing Prompt Template

**Role**: Senior Developer
**Task**: Add clear and concise inline comments to the given [LANGUAGE] code to improve readability for other developers.
**Input Placeholder**: [CODE_BLOCK]
**Expected Output**: The same code with meaningful inline comments explaining non-obvious logic, decisions, and complex operations.

---

## Example Prompt

You are a senior developer improving code readability.
Add clear inline comments to the following [LANGUAGE] code.
Focus on explaining the why, not just the what.
Do not comment on obvious lines.

\`\`\`
[CODE_BLOCK]
\`\`\`

Return the fully commented code without changing any logic.'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\prompt_patterns_library\prompts\inline_comments.md', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
"