python -c "
content = '''async function getUserNames(url) {
    const response = fetch(url);
    const data = response.json();
    const names = data.map(user => user.name.toUpperCase());
    return names;
}

const result = getUserNames('https://jsonplaceholder.typicode.com/users');
console.log('Names:', result);
'''
with open(r'C:\Users\Fatima\OneDrive\Desktop\bug_descriptions.md\smart_bug_bounty\bug_snippets\bug4.js', 'w') as f:
    f.write(content)
print('Done')
"