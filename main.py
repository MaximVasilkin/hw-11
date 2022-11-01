import requests
from bs4 import BeautifulSoup


def scraping(keywords):
    url = 'https://habr.com/ru'
    headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36')}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, features='html.parser')
    articles = soup.find_all(class_='tm-articles-list__item')
    for article in articles:
        if any([keyword in article.text or keyword.capitalize() in article.text for keyword in keywords]):
            date = article.find(class_='tm-article-snippet__datetime-published').text
            title = article.find(class_='tm-article-snippet__title-link')
            href = url + title.attrs['href'][3:]
            border = '*' * 30
            print(f'Дата: {date}\nЗаголовок: {title.text}\nСсылка: {href}\n{border}')


if __name__ == '__main__':
    scraping(['дизайн', 'фото', 'web', 'python'])
