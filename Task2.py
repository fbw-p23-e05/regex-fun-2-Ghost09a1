import re

text = "Exercises number 1, 12, 13, and 345 are important"
numbers = re.findall(r'\b\d{1,3}\b', text)
print(numbers)
