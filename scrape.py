import requests
from Article import *
from bs4 import BeautifulSoup
import matplotlib.pyplot as mpl


def scrape(url, articleClass, int_Where_In_URL_is_Category, int_Where_in_URL_is_SubCategory, meta_data_class=None):
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
            article_title_elem = article.find('h2', {'class': f'{articleClass}'})
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

def themeify(url,int_Where_In_URL_is_Category, int_Where_in_URL_is_SubCategory,):

    parts = url.split('/')
    category = parts[int_Where_In_URL_is_Category]
    sub_category = parts[int_Where_in_URL_is_SubCategory]
    return category, sub_category

def countPhrases(list_of_article_objects, phraseToCount):
    hits = []
    for article in range(list_of_article_objects):
        if phraseToCount in list_of_article_objects.text:
            hits.append(article)
    return len(hits)

def countWord(list_of_article_objects, wordToCount):

    hits = []
    for article in range(list_of_article_objects):
        if wordToCount in list_of_article_objects.text:
            hits.append(article)
    return len(hits)

def findArticlesWithPhrase(list_of_article_objects, phraseToFind):
    hits = []
    for article in range(list_of_article_objects):
        if phraseToFind in list_of_article_objects.text:
            hits.append(article)
    return prettyPrint(hits)

def findArticlesWithWord(list_of_article_objects, wordToFind):

    hits = []
    for article in range(list_of_article_objects):
        if wordToFind in list_of_article_objects.text:
            hits.append(article)
    return prettyPrint(hits)


def compareNewsWebsistes(list_of_article_objects, list_of_article_objects_2nd_website, word=None, phrase=None,
                         url_website_1=None, url_website_2=None,
                         metadata_class_url_one=None, metadata_class_url_two=None):

    if phrase is not None:
        website_1_phrase = countPhrases(list_of_article_objects, phrase)
        website_2_phrase = countPhrases(list_of_article_objects_2nd_website, phrase)
        if website_1_phrase > website_2_phrase:
            print(f"The first website has more occurences of the phrase: {phrase} with {website_1_phrase} occurences vs. the other websites: {website_2_phrase}\n")
        elif website_2_phrase > website_1_phrase:
            print(f"The second website has more occurences of the phrase: {phrase} with {website_2_phrase} occurences vs. the other websites: {website_1_phrase}\n")
        elif website_2_phrase == website_1_phrase:
            print(f"Both websites have the same number of occurances of {phrase}, with {website_1_phrase} occurences each\n")

    if word is not None:
        website_1_word = countPhrases(list_of_article_objects, word)
        website_2_word = countPhrases(list_of_article_objects_2nd_website, word)
        if website_1_word > website_2_word:
            print(f"The first website has more occurences of the word: {word} with {website_1_word} occurences vs. the other websites: {website_2_word}\n")
        elif website_2_word > website_1_word:
            print(f"The second website has more occurences of the word: {word} with {website_2_word} occurences vs. the other websites: {website_1_word}\n")
        elif website_2_word == website_1_word:
            print(f"Both websites have the same number of occurances of {word}, with {website_1_word} occurences each\n")

    if url_website_1 and url_website_2 is not None:
        if metadata_class_url_one and metadata_class_url_two is not None:
            website_1_metaData = countMetadata(url_website_1, metadata_class_url_one)
            website_2_metaData = countMetadata(url_website_2, metadata_class_url_two)
            if website_1_metaData > website_2_metaData:
                print(
                    f"The first website has more occurences of metadata with {website_1_metaData} occurences vs. the other websites: {website_2_metaData}\n")
            elif website_2_metaData > website_1_metaData:
                print(
                    f"The second website has more occurences of metadata with {website_2_metaData} occurences vs. the other websites: {website_1_metaData}\n")
            elif website_2_metaData == website_1_metaData:
                print(
                    f"Both websites have the same number of occurances of metadata, with {website_1_metaData} occurences each\n")

    print("The two websites have the following spread of categories: ")
    print(f"The 1st website: {countCategories(list_of_article_objects)}")
    print(f"The 2nd website: {countCategories(list_of_article_objects_2nd_website)}")


def countCategories(list_of_article_objects):

    article_counts = {}
    for article in list_of_article_objects:
        category = article.category
        if category in article_counts:
            article_counts[category] += 1
        else:
            article_counts[category] = 1

    print(article_counts)
    return article_counts


def countSubCategories(list_of_article_objects):

    article_counts = {}
    for article in list_of_article_objects:
        sub_category = article.sub_category
        if sub_category in article_counts:
            article_counts[sub_category] += 1
        else:
            article_counts[sub_category] = 1

    print(article_counts)
    return article_counts


def compareHTMLCode(url1, url2):
    #TODO: find diffrences
    #TODO: the function itself
    pass

def countMetadata(webpage, metadata_class):
    #TODO: add logic of the function
    pass


def compareMetadata(page1, page2, metadata_class_website_one, metadata_class_website_two):

    metaCount1 = countMetadata(page1, metadata_class_website_one)
    metaCount2 = countMetadata(page2, metadata_class_website_two)

    if metaCount1 > metaCount2:
        return "Page 1 has more metadata"
    elif metaCount2 > metaCount1:
        return "Page 2 has more metadata"
    else:
        return "Both pages have the same amount of metadata"

def prettyPrint(list):
    for item in range(list):
        print(f"{item}\n")


def printPieChart(dictionary):

    labels = list(dictionary.keys())
    values = list(dictionary.values())

    mpl.pie(values, labels=labels, autopct='%1.1f%%')
    mpl.axis('equal')

    mpl.show()


def printPieChartFromLists(listOfLabels, listOfValues):
    labels = list(listOfLabels)
    values = list(listOfValues)

    mpl.pie(values, labels=labels, autopct='%1.1f%%')
    mpl.axis('equal')

    mpl.show()

