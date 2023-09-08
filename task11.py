import re
text = 'The price is $12.34, and the quantity is 5.'
numbers = re.findall(r'\d+\.\d+|\d+', text)
print(numbers)
