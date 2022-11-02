import requests
from bs4 import BeautifulSoup


def scraping(keywords):
    url = 'https://habr.com/ru'
    headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36')}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, features='html.parser')
    articles = soup.find_all(class_='tm-articles-list__item')

    def _match(text, loop=True):
        if any([keyword in text or keyword.capitalize() in text for keyword in keywords]):
            print(f'Дата: {date}\nЗаголовок: {title.text}\nСсылка: {href}\n{border}')
        elif loop:
            response = requests.get(href, headers=headers)
            text_soup = BeautifulSoup(response.text, features='html.parser')
            text_ = text_soup.find(id='post-content-body').text
            _match(text_, False)

    for article in articles:
        date = article.find(class_='tm-article-snippet__datetime-published').text
        title = article.find(class_='tm-article-snippet__title-link')
        href = url + title.attrs['href'][3:]
        border = '*' * 30
        _match(article.text)


if __name__ == '__main__':
    scraping(['дизайн', 'фото', 'web', 'python'])
