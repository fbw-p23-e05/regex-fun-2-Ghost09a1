import re

url = 'https://example.com/2023/09/08/page'
match = re.search(r'/(\d{4})/(\d{2})/(\d{2})/', url)
if match:
    year, month, day = match.groups()
    print(f'Year: {year}, Month: {month}, Day: {day}')
