import requests
import json

url = 'http://openlibrary.org/search.json'

subject = 'Artificial intelligence'

params = {
    'subject': subject,
    'Limit': 1
}

response = requests.get(url, params)

if response.status_code == 200:
    print('Успешный запрос')
else:
    print('Запрос Api откланен с кодом состояния:', response.status_code)

data = json.loads(response.text)

books = data['docs']
for book in books:
    print('Title:', book['title'])
    print('Author:', book['author_name'])
    print('Subject:', book['subject'])
    print('\n')