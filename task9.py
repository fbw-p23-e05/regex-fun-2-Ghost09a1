import re
date_str = '2023-09-08'
formatted_date = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', date_str)
print(formatted_date)
