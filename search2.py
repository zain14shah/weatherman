"""
Display all words and their frequency in a txt file.
"""
import re
from collections import defaultdict

file_data = open('words2.txt').read()

word_count = defaultdict(int)

words = re.findall(r'\b\w+\b', file_data)

for word in words:
	word_count[word] += 1

for key, value in word_count.items():
	print('{} appears {} times.'.format(key, value))

