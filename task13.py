import re
text = 'The price is $12.34, and the quantity is 5.'
matches = [(match.group(), match.start()) for match in re.finditer(r'\d+\.\d+|\d+', text)]
print(matches)
