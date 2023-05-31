import requests
import urllib.parse
import http.client
import concurrent.futures
from urllib.parse import urljoin, urlparse
import re


class Scraper:
    @staticmethod
    def scrape(url, data_type):
        """Scrapes data from a given URL.

        Args:
            url (str): The URL to scrape.
            data_type (str): The type of data to scrape ('html' or 'json').

        Returns:
            bytes or dict: The scraped data.

        Raises:
            ValueError: If an unsupported data type is provided.
            Exception: If the request fails with a non-200 status code.

        Example:
            scraper = Scraper()
            html_content = scraper.scrape('https://example.com', 'html')
            json_data = scraper.scrape('https://example.com/api', 'json')
        """
        session = requests.Session()
        response = session.get(url)
        if response.status_code == 200:
            if data_type == 'html':
                return response.content
            elif data_type == 'json':
                return response.json()
            else:
                raise ValueError(f"Unsupported data type: {data_type}")
        else:
            raise Exception(f"Request failed with status code {response.status_code}")


class WebScraper:
    """A web crawler for scraping and extracting URLs from web pages."""

    def __init__(self):
        self.scraper = Scraper()

    def scrape(self, url, data_type):
        """Scrapes data from a given URL.

        Args:
            url (str): The URL to scrape.
            data_type (str): The type of data to scrape ('html' or 'json').

        Returns:
            str or dict: The scraped data as a string (HTML) or a dictionary (JSON).

        Example:
            web_scraper = WebScraper()
            html_content = web_scraper.scrape('https://example.com', 'html')
            json_data = web_scraper.scrape('https://example.com/api', 'json')
        """
        content = self.scraper.scrape(url, data_type)
        if data_type == 'html':
            return content.decode('utf-8')  # Decode content into a string
        return content

    def extract_urls(self, html_content, parsed_url):
        """Extracts URLs from the HTML content.

                Args:
                    html_content (str): The HTML content to extract URLs from.
                    parsed_url (urllib.parse.ParseResult): The parsed URL of the web page.

                Returns:
                    list: A list of extracted URLs.

                Example:
                    crawler = WebCrawler()
                    html_content = crawler.scrape('https://example.com')
                    parsed_url = crawler.parse_url('https://example.com')
                    urls = crawler.extract_urls(html_content, parsed_url)
                    for url in urls:
                        print(url)
                """

        start_tag = '<a'
        end_tag = '</a>'
        href_attr = 'href='
        url_prefixes = ('http://', 'https://')

        urls = []

        while True:
            start_index = html_content.find(start_tag)
            if start_index == -1:
                break

            end_index = html_content.find(end_tag, start_index)
            if end_index == -1:
                break

            anchor_content = html_content[start_index:end_index]
            href_index = anchor_content.find(href_attr)
            if href_index == -1:
                continue

            href_start = anchor_content.find('"', href_index) + 1
            href_end = anchor_content.find('"', href_start)
            href = anchor_content[href_start:href_end]

            if href.startswith(url_prefixes):
                urls.append(href)
            else:
                absolute_url = urljoin(parsed_url.geturl(), href)
                urls.append(absolute_url)

            html_content = html_content[end_index:]

        return urls


class WebCrawler:
    """A web crawler for scraping and extracting URLs from web pages."""

    def __init__(self):
        self.visited_urls = set()
        self.queue = []

    def crawl(self, url, max_depth=3, num_threads=5):
        """Crawl the web starting from a given URL.

        Args:
            url (str): The starting URL to crawl.
            max_depth (int, optional): The maximum depth to crawl. Defaults to 3.
            num_threads (int, optional): The number of threads to use for concurrent crawling. Defaults to 5.

        Returns:
            list: A list of crawled URLs.

        Example:
            crawler = WebCrawler()
            crawled_urls = crawler.crawl('https://example.com', max_depth=2, num_threads=10)
            for url in crawled_urls:
                print(url)
        """
        crawled_urls = []
        visited_urls = set()
        queue = [(url, 0)]

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
            while queue:
                current_url, depth = queue.pop(0)

                if depth > max_depth:
                    continue

                if current_url not in visited_urls:
                    visited_urls.add(current_url)
                    print(f"Crawling {current_url} at depth {depth}")

                    try:
                        html_content = self.scrape(current_url, 'html')
                        print(f"HTML content: {html_content}")
                        parsed_urls = self.extract_urls(html_content, current_url)
                        print(f"Parsed URLs: {parsed_urls}")
                        crawled_urls.append(current_url)

                        for parsed_url in parsed_urls:
                            queue.append((parsed_url, depth + 1))
                    except Exception as e:
                        print(f"Error occurred while crawling {current_url}: {str(e)}")

                return crawled_urls

    def scrape(self, url, data_type):
        web_scraper = WebScraper()
        return web_scraper.scrape(url, data_type)

    def parse_html(self, url, html_content):
        """Parses the HTML content and extracts URLs.

               Args:
                   url (str): The URL of the web page.
                   html_content (str): The HTML content to parse.

               Returns:
                   list: A list of extracted URLs.

               Example:
                   crawler = WebCrawler()
                   html_content = crawler.scrape('https://example.com')
                   urls = crawler.parse_html('https://example.com', html_content)
                   for url in urls:
                       print(url)
               """
        start_tag = '<a'
        end_tag = '</a>'
        href_attr = 'href='
        url_prefixes = ('http://', 'https://')

        urls = []

        while True:
            start_index = html_content.find(start_tag)
            if start_index == -1:
                break

            end_index = html_content.find(end_tag, start_index)
            if end_index == -1:
                break

            anchor_content = html_content[start_index:end_index]
            href_index = anchor_content.find(href_attr)
            if href_index == -1:
                continue

            href_start = anchor_content.find('"', href_index) + 1
            href_end = anchor_content.find('"', href_start)
            href = anchor_content[href_start:href_end]

            if href.startswith(url_prefixes):
                urls.append(href)
            else:
                absolute_url = urljoin(url, href)
                urls.append(absolute_url)

            html_content = html_content[end_index:]

        # Example: Print extracted URLs
        for url in urls:
            print(url)

    def extract_urls(self, html_content, base_url):
        """Extracts URLs from the HTML content.

               Args:
                   html_content (str): The HTML content to extract URLs from.
                   base_url (str): The base URL of the web page.

               Returns:
                   list: A list of extracted URLs.

               Example:
                   crawler = WebCrawler()
                   html_content = crawler.scrape('https://example.com')
                   urls = crawler.extract_urls(html_content, 'https://example.com')
                   for url in urls:
                       print(url)
               """
        start_tag = '<a'
        end_tag = '</a>'
        href_attr = 'href='
        url_prefixes = ('http://', 'https://')

        urls = []

        parsed_base_url = urlparse(base_url)

        while True:
            start_index = html_content.find(start_tag)
            if start_index == -1:
                break

            end_index = html_content.find(end_tag, start_index)
            if end_index == -1:
                break

            anchor_content = html_content[start_index:end_index]
            href_index = anchor_content.find(href_attr)
            if href_index == -1:
                continue

            href_start = anchor_content.find('"', href_index) + 1
            href_end = anchor_content.find('"', href_start)
            href = anchor_content[href_start:href_end]

            if href.startswith(url_prefixes):
                urls.append(href)
            else:
                absolute_url = urljoin(parsed_base_url.geturl(), href)
                urls.append(absolute_url)

            html_content = html_content[end_index:]
        print(urls)
        return urls


class ElementSelector:
    @staticmethod
    def extract_elements(html, selector):
        """Extracts elements from the HTML based on the provided selector."""
        if selector.startswith("//"):
            # XPath selector
            return ElementSelector.extract_elements_by_xpath(html, selector)
        elif selector.startswith("<"):
            # HTML tag selector
            return ElementSelector.extract_elements_by_tag(html, selector)
        else:
            # CSS selector
            return ElementSelector.extract_elements_by_css_selector(html, selector)

    @staticmethod
    def extract_elements_by_xpath(html, selector):
        """Extracts elements from the HTML based on the provided XPath selector."""
        pattern = r'<[^>]*>'
        elements = re.findall(pattern, html)
        return elements

    @staticmethod
    def extract_elements_by_tag(html, selector):
        """Extracts elements from the HTML based on the provided HTML tag selector."""
        tag_name = selector[1:-1]
        pattern = rf'<{tag_name}[^>]*>'
        elements = re.findall(pattern, html)
        return elements

    @staticmethod
    def extract_elements_by_css_selector(html, selector):
        """Extracts elements from the HTML based on the provided CSS selector."""
        selector = selector.strip()
        selector_parts = selector.split(" ")

        elements = [html]
        for part in selector_parts:
            if part.startswith("#"):
                # Extract by ID
                id_value = part[1:]
                elements = ElementSelector.filter_elements_by_attribute(elements, "id", id_value)
            elif part.startswith("."):
                # Extract by class
                class_value = part[1:]
                elements = ElementSelector.filter_elements_by_attribute(elements, "class", class_value)
            elif part.startswith("["):
                # Extract by attribute
                attr_match = re.match(r"\[(.*)=(.*)\]", part)
                if attr_match:
                    attr_name, attr_value = attr_match.group(1), attr_match.group(2)
                    elements = ElementSelector.filter_elements_by_attribute(elements, attr_name, attr_value)

        return elements

    @staticmethod
    def filter_elements_by_attribute(elements, attr_name, attr_value):
        """Filters elements based on the provided attribute name and value."""
        filtered_elements = []
        for element in elements:
            pattern = rf'{attr_name}=[\'"]{attr_value}[\'"]'
            if re.search(pattern, element):
                filtered_elements.append(element)
        return filtered_elements

