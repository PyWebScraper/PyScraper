import requests
from Article import *
from bs4 import BeautifulSoup as soup

def scrape(url, request_function=requests.get):
    # HTTP Get request to the given URL
    response = requests.get(url)

    # if request is successful we will get status code 200
    if response.status_code == 200:

            # Scrape the articles and create Article objects
            articles = []
            for article in soup.find_all('a', {'class': 'article-link'}):
                article_url = article['href']
                category, sub_category = themeify(article_url)
                title = article.find('h2', {'class': 'article-title'}).text.strip()
                date = article.find('time', {'class': 'article-time'})['datetime']
                content = scrape(article_url)
                # ...
                articles.append(Article(category, sub_category, title, date, content))

            return articles



    # If the request was not successful, raise an exception
    else:
        raise Exception('Request failed with status code {}'.format(response.status_code))

def themeify(url):
    parts = url.split('/')
    category = parts[3]
    sub_category = parts[4]
    return category, sub_category