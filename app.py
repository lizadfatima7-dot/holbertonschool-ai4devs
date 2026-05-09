import re
from collections import Counter

with open('sample.txt', 'r') as f:
    text = f.read()

words = re.findall(r'\b\w+\b', text.lower())
word_count = len(words)
top_5 = Counter(words).most_common(5)

print(f'Total words: {word_count}')
print('Top 5 most common words:')
for word, count in top_5:
    print(f'  {word}: {count}')