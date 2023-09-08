import re
text = 'Hello, World. This is a test!'
replaced_text = re.sub(r'[ ,.]', ':', text, count=2)
print(replaced_text)
