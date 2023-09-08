import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
matches = re.findall(pattern, text)
print(matches)
