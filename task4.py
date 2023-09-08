import re
text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'
match = re.search(searched_word, text)
if match:
    print(f"'{searched_word}' found at position {match.start()}")
else:
    print(f"'{searched_word}' not found in the text.")
