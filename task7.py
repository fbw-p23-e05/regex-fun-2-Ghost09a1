import re
text = 'Hello World'
underscored_text = re.sub(r'\s', '_', text)
space_text = re.sub(r'_', ' ', underscored_text)
print(underscored_text)
print(space_text)