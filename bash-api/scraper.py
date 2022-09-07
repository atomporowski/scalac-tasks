import requests
from bs4 import BeautifulSoup

page = 1
jokes_list = []

while len(jokes_list) < 100:
    url = f'http://bash.org.pl/latest/?page={page}'
    # Connecting to the website and getting its content
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # Getting all divs with jokes
    jokes = soup.find_all('div', class_='q post')

    for joke in jokes:
        body = joke.find('div', class_='quote post-content post-body').text.strip()
        date = joke.find('div', class_='right').text.strip()
        id = joke.find('a', class_='qid click').text.strip()[1:]
        points = joke.find('span', class_='points').text.strip()

        joke_details = {
            'id': id,
            'body': body,
            'date': date,
            'points': points
        }

        jokes_list.append(joke_details)

    page += 1

# Remove comment to check number of jokes
# print(len(jokes_list))
