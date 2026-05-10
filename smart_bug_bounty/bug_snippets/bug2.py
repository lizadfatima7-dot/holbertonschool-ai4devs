python -c "
content = '''def factorial(n):
    if n == 1:
        return 1
    result = 0
    for i in range(1, n):
        result *= i
    return result

print(factorial(5))
print(factorial(1))
print(factorial(0))
'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\smart_bug_bounty\bug_snippets\bug2.py', 'w') as f:
    f.write(content)
print('Done')
"