python -c "
content = '''function average(numbers) {
    const valid = numbers.filter(n => typeof n === 'number');
    const sum = valid.reduce((acc, n) => acc + n);
    return (sum / valid.length).toFixed(2);
}

console.log(average([1, 2, 3, 4, 5]));
console.log(average([10, 'hello', null, 20]));
console.log(average([]));
'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\smart_bug_bounty\bug_snippets\bug3.js', 'w') as f:
    f.write(content)
print('Done')
"