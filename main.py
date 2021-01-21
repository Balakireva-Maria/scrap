import requests
from bs4 import BeautifulSoup
keywords = ['дизайн', 'фото', 'web', 'python']
url = 'https://habr.com/ru/all/'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
hubs_list = []

for article in (soup.find_all('article', class_='post')):
    hubs_list.append((article.find('a', class_='hub-link').text.lower()))


for word in keywords:
    if word in hubs_list:
        time = article.find('span', class_='post__time').text
        title = article.find('h2', class_='post__title').text
        link = article.find('a', class_='post__title_link').get('href')
        print(f' {time} - {title} - {link}')












