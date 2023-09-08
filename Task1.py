import re

text = "Hello World 123"
result = bool(re.search(r'\d$', text))
print(result)
