import re
text = 'Hello, World. This is a test!'
replaced_text = re.sub(r'[ ,.]', ':', text)
print(replaced_text)
