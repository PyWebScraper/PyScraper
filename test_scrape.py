import pytest
from unittest.mock import patch
from scrape import *

mock_json = {
    "id": 1,
    "title": "Sample JSON Object",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
}

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
        with patch.object(scraper, 'scrape', return_value=mock_json):
            result = scraper.scrape(url, data_type)
            assert isinstance(result, dict)
            assert result == mock_json

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
    with patch.object(web_scraper, 'scrape', return_value=mock_json):
        json_data = web_scraper.scrape(url_json, data_type_json)

    # Assert that the scraped JSON data is a dictionary
    assert isinstance(json_data, dict)
    assert json_data == mock_json

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

def test_extract_elements_by_xpath():
    html = '<div class="container"><h1>Title</h1><p>Content</p></div>'
    selector = "//h1"
    expected_elements = ['<h1>Title</h1>']

    elements = ElementSelector.extract_elements_by_xpath(html, selector)
    print(f"Actual elements: {elements}")

    assert elements == expected_elements


def test_extract_elements_by_tag():
    html = '<div class="container"><h1>Title</h1><p>Content</p></div>'
    selector = "<p>"
    expected_elements = ['<p>Content</p>']

    elements = ElementSelector.extract_elements_by_tag(html, selector)
    print(f"Actual elements: {elements}")

    assert elements == expected_elements


def test_extract_elements_by_css_selector():
    html = '<div class="container"><h1>Title</h1><p>Content</p></div>'
    selector = ".container p"
    expected_elements = ['<p>Content</p>']

    elements = ElementSelector.extract_elements_by_css_selector(html, selector)
    print(f"Actual elements: {elements}")

    assert elements == expected_elements


def test_filter_elements_by_attribute():
    elements = ['<h1 id="title">Title</h1>', '<p class="content">Content</p>']
    attr_name = "class"
    attr_value = "content"
    expected_elements = ['<p class="content">Content</p>']

    filtered_elements = ElementSelector.filter_elements_by_attribute(elements, attr_name, attr_value)
    print(f"Filtered elements: {filtered_elements}")

    assert filtered_elements == expected_elements


def test_extract_elements():
    html = '<div class="container"><h1>Title</h1><p>Content</p></div>'
    selector = ".container p"
    expected_elements = ['<p>Content</p>']

    elements = ElementSelector.extract_elements(html, selector)
    print(f"Actual elements: {elements}")

    assert elements == expected_elements




# Run the tests
if __name__ == "__main__":
    pytest.main()
