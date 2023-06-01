import pytest
from unittest.mock import patch
from scrape import *

# Test the Scraper class
class TestScraper:
    def test_scrape_html(self):
        url = "https://example.com"
        data_type = "html"
        scraper = Scraper()
        result = scraper.scrape(url, data_type)
        assert isinstance(result, bytes)

    def test_scrape_json(self):
        url = "https://example.com"
        data_type = "json"
        scraper = Scraper()
        result = scraper.scrape(url, data_type)
        assert isinstance(result, dict)

    def test_scrape_unsupported_type(self):
        url = "https://example.com"
        data_type = "unsupported"
        scraper = Scraper()
        with pytest.raises(ValueError):
            scraper.scrape(url, data_type)


def test_extract_urls():
    html_content = """
    <html>
        <body>
            <a href="https://example.com/page1">Page 1</a>
            <a href="/page2">Page 2</a>
            <a href="https://example.com/page3">Page 3</a>
        </body>
    </html>
    """
    base_url = "https://example.com"

    expected_urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
    ]

    # Call the function to extract URLs
    extracted_urls = extract_urls(html_content, base_url)

    # Assert that the extracted URLs match the expected URLs
    assert extracted_urls == expected_urls


def test_parse_html():
    url = "https://example.com"
    html_content = """
    <html>
        <body>
            <a href="https://example.com/page1">Page 1</a>
            <a href="/page2">Page 2</a>
            <a href="https://example.com/page3">Page 3</a>
        </body>
    </html>
    """
    expected_urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3"
    ]

    # Call the function to parse HTML and extract URLs
    extracted_urls = parse_html(url, html_content)

    # Assert that the extracted URLs match the expected URLs
    assert extracted_urls == expected_urls


def test_web_scraper():
    # Create an instance of WebScraper
    web_scraper = WebScraper()

    # Test scraping HTML content
    url_html = "https://example.com"
    data_type_html = "html"
    html_content = web_scraper.scrape(url_html, data_type_html)

    # Assert that the scraped HTML content is a string
    assert isinstance(html_content, str)

    # Test scraping JSON data
    url_json = "https://example.com/api"
    data_type_json = "json"
    json_data = web_scraper.scrape(url_json, data_type_json)

    # Assert that the scraped JSON data is a dictionary
    assert isinstance(json_data, dict)

def test_crawl_single_page():
    # Create an instance of WebCrawler
    crawler = WebCrawler()

    # Patch the scrape method to return a dummy HTML content
    with patch.object(crawler, 'scrape',
                      return_value='<html><body><a href="https://example.com/page1">Page 1</a></body></html>'):
        # Perform the crawl
        crawled_urls = crawler.crawl('https://example.com', max_depth=1, num_threads=1)

        # Assert that the crawled URLs contain the starting URL and the extracted URL
        assert 'https://example.com' in crawled_urls
        assert 'https://example.com/page1' in crawled_urls


def test_crawl_multiple_pages():
    # Create an instance of WebCrawler
    crawler = WebCrawler()

    # Patch the scrape method to return dummy HTML content for different URLs
    with patch.object(crawler, 'scrape',
                      side_effect=['<html><body><a href="https://example.com/page1">Page 1</a></body></html>',
                                   '<html><body><a href="https://example.com/page2">Page 2</a></body></html>']):
        # Perform the crawl
        crawled_urls = crawler.crawl('https://example.com', max_depth=2, num_threads=1)

        # Assert that the crawled URLs contain the starting URL and the extracted URLs
        assert 'https://example.com' in crawled_urls
        assert 'https://example.com/page1' in crawled_urls
        assert 'https://example.com/page2' not in crawled_urls  # Updated assertion



def test_crawl_with_error():
    # Create an instance of WebCrawler
    crawler = WebCrawler()

    # Patch the scrape method to raise an exception
    with patch.object(crawler, 'scrape', side_effect=Exception("Scrape error")):
        # Perform the crawl
        crawled_urls = crawler.crawl('https://example.com', max_depth=1, num_threads=1)

        # Assert that no URLs were crawled due to the error
        assert len(crawled_urls) == 0


# Run the tests
if __name__ == "__main__":
    pytest.main()
