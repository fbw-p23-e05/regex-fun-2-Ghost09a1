import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
matches = [(match.group(), match.start()) for match in re.finditer(pattern, text)]
print(matches)
