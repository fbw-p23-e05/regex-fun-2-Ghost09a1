import re
text = 'Apple is an example of a fruit, and elephant is an example of an animal.'
matches = re.findall(r'\b[aeAE]\w+', text)
print(matches)