from Article import Article
from scrape import *


def test_scrape_website():
    # Define a test request function that returns a test HTML response
    def test_request(url):
        return b'<html><head><title>Test Title</title></head><body><p>Test Content</p></body></html>'

    # Call the scrape_website function with the test request function
    articles = scrape('https://www.example.com', request_function=test_request)

    # Check that the scraped articles have the expected properties
    assert len(articles) == 1
    article = articles[0]
    assert article.title == 'Test Title'
    assert article.content == 'Test Content'


def test_themeify():
    url = 'https://www.vg.no/nyheter/innenriks/i/abc123/norge-faar-nytt-parti'
    category, sub_category = themeify(url)
    assert category == 'nyheter'
    assert sub_category == 'innenriks'