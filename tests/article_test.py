from Article import *
import scrape


def scrape_website():
    # This function simulates scraping a website
    article1 = Article("Article 1", "Sports", "football", "https://www.example.com/article1", "2022-01-01")
    article2 = Article("Article 2", "Science", "geology", "https://www.example.com/article2", "2022-01-02",
                       "Python is cool")
    article3 = Article("Article 3", "Politics", "election", "https://www.example.com/article3", "2022-01-03", "2022-01-04",
                       "Data analysis")
    return [article1, article2, article3]


# Testing the functionality of the scrape function as well as the article class and the value it holds.

def test_scrape_website():
    # This function tests the scrape_website function
    articles = scrape.scrape()
    assert len(articles) == 3

    assert articles[0].title == "Article 1"
    assert articles[0].category == "Sports"
    assert articles[0].sub_category == "football"
    assert articles[0].url == "https://www.example.com/article1"
    assert articles[0].date_published == "2022-01-01"
    assert articles[0].date_updated is None
    assert articles[0].most_repeated_phrase is None

    assert articles[1].title == "Article 2"
    assert articles[1].category == "Science"
    assert articles[1].sub_category == "geology"
    assert articles[1].url == "https://www.example.com/article2"
    assert articles[1].date_published == "2022-01-02"
    assert articles[1].date_updated is None
    assert articles[1].most_repeated_phrase == "Python is cool"

    assert articles[2].title == "Article 3"
    assert articles[2].category == "Politics"
    assert articles[2].sub_category == "election"
    assert articles[2].url == "https://www.example.com/article3"
    assert articles[2].date_published == "2022-01-03"
    assert articles[2].date_updated == "2022-01-04"
    assert articles[2].most_repeated_phrase == "Data analysis"
