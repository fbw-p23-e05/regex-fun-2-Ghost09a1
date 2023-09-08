import re 
word_list = ['Python', 'Perl', 'Java', 'C++']
matches = [word for word in word_list if re.match(r'^P', word)]
print(matches)
