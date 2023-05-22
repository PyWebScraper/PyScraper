import requests
from Article import *
from bs4 import BeautifulSoup


#TODO: summary of comparison to PDF
#TODO: all articles in category X with different parameters for aplhabetical, by publish date/time, ++
#TODO: Sumarize ad to Article ratio (how many articles is there per ad)
#TODO: add extraction of date/time published
#TODO: add extraction of date/time updated

def scrape(url, article_class, int_Where_In_URL_is_Category, int_Where_in_URL_is_SubCategory, meta_data_class=None):
    # HTTP Get request to the given URL
    response = requests.get(url)

    # if request is successful we will get status code 200
    print(response.status_code)
    if response.status_code == 200:

        # Create a BeautifulSoup object from the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape the articles and create Article objects
        articles = []

        for article in soup.find_all(class_="article"):
            print(article)
            article_url_elem = article.find('a')
            if article_url_elem is not None:
                article_url = article_url_elem['href']
                # Extract category and subcategory from article URL
                url_parts = article_url.split('/')
                # Both category and subcategory needs a try except, in case urls are formated diffrently
                try:
                    category = url_parts[int_Where_In_URL_is_Category]
                except:
                    category = None
                try:
                    sub_category = url_parts[int_Where_in_URL_is_SubCategory]
                except:
                    sub_category = None
            else:
                article_url = None
                category = None
                sub_category = None

            # category, sub_category = themeify(article_url)
            article_title_elem = article.find('h2', {'class': f'{article_class}'})
            if article_title_elem is not None:
                article_title_in_pieces = article_title_elem.find_all('span')
                title = ' '.join([element.text for element in article_title_in_pieces])
            else:
                title = None

            if meta_data_class is not None:
                script_tag = article.find('script', {'class': f'{meta_data_class}'})

            date_published = None
            time_published = None
            time_updated = None
            date_updated = None
            articles.append(Article(title=title, date_published=date_published,
                                    date_updated=date_updated, url=article_url,
                                    category=category, sub_category=sub_category))

            #articles.append(Article(category, sub_category, title, date, content))

    # If the request was not successful, raise an exception
    else:
        raise Exception('Request failed with status code {}'.format(response.status_code))

    for article in articles:
        print(article)
    return articles



