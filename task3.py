text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']
found_words = [word for word in searched_words if word in text]
print(found_words)
