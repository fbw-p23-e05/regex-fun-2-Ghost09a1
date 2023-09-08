import re
text = '123 Main Road, Apt 4B'
abbreviated_text = re.sub(r'\bRoad\b', 'Rd.', text)
print(abbreviated_text)
