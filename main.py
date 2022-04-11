import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    r = requests.get('https://quotes.toscrape.com/random')
    print(r)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    s = soup.find('div', class_='quote')
    quotes = s.find_all('span', class_ ='text')
    authors = s.find_all('small',class_ ='author')
    
    for quote in zip(quotes,authors):
        print(f'{quote[0].text} \nby {quote[1].text}')
    # tags = s.find_all('a', class_='tag')
    # for link in tags:
    #     print(link.get('href'))
