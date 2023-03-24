import requests
from Article import *
from bs4 import BeautifulSoup


def scrape(url):
    # HTTP Get request to the given URL
    response = requests.get(url)

    # if request is successful we will get status code 200

    if response.status_code == 200:

        # Create a BeautifulSoup object from the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape the articles and create Article objects
        articles = []

        for article in soup.find_all(class_="article"):
            #print(article)
            article_url_elem = article.find('a')
            if article_url_elem is not None:
                article_url = article_url_elem['href']
                # Extract category and subcategory from article URL
                url_parts = article_url.split('/')
                # Both category and subcategory needs a try except, in case urls are formated diffrently
                try:
                    category = url_parts[3]
                except:
                    category = None
                try:
                    sub_category = url_parts[4]
                except:
                    sub_category = None
            else:
                article_url = None
                category = None
                sub_category = None

            # category, sub_category = themeify(article_url)
            article_title_elem = article.find('h2', {'class': 'headline'})
            if article_title_elem is not None:
                article_title_in_pieces = article_title_elem.find_all('span')
                title = ' '.join([element.text for element in article_title_in_pieces])
            else:
                title = None

            script_tag = article.find('script', {'class': 'tracking-data'})

            date_published = None
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

def themeify(url):

    parts = url.split('/')
    category = parts[3]
    sub_category = parts[4]
    return category, sub_category

def countPhrases(list_of_article_objects):
    #TODO: add countPhrases function
    pass

def compareNewsWebsistes(list_of_article_objects, list_of_article_objects_2nd_website ):
    #TODO: Add compareNewsWebsites function
    #TODO: news to accept an argument for categories
    pass

def compareHTMLCode(url1, url2):
    #TODO: find diffrences
    #TODO: the function itself
    pass

def countMetadata(webpage):
    #TODO: add logic of the function
    pass

def compareMetadata(page1, page2):

    metaCount1 = countMetadata(page1)
    metaCount2 = countMetadata(page2)

    if metaCount1 > metaCount2:
        return "Page 1 has more metadata"
    elif metaCount2 > metaCount1:
        return "Page 2 has more metadata"
    else:
        return "Both pages have the same amount of metadata"
