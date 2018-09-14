"""

"""
import re

input_text = input('Please enter what you want to find: ')

try:
	file_data = open('words.txt').read()
except UnicodeDecodeError:
	print('File reading failed')

match = re.findall(r'\b{}\b'.format(input_text), file_data)

if match:
	print('Found')
	print('Number of times it occurs: ')
	print(len(match))
else:
	print("Not found")
