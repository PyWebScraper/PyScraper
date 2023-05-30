import requests
import urllib.parse
import http.client
from urllib.parse import urljoin


class WebScraper:
    """A web crawler for scraping and extracting URLs from web pages."""

    def __init__(self):
        self.session = requests.Session()
        self.visited_urls = set()
        self.queue = []

    def scrape(self, url, data_type):
        """Scrapes the content of the specified URL.

                Args:
                    url (str): The URL to scrape.

                Returns:
                    str: The scraped HTML content.

                Raises:
                    Exception: If the request fails or returns a non-200 status code.
                """

        response = self.session.get(url)
        if response.status_code == 200:
            if data_type == 'html':
                return response.content
            elif data_type == 'json':
                return response.json()
            else:
                raise ValueError(f"Unsupported data type: {data_type}")
        else:
            raise Exception(f"Request failed with status code {response.status_code}")

    def crawl(self, start_url, depth=1):
        """Crawls web pages starting from the specified URL.

               Args:
                   start_url (str): The starting URL to crawl from.
                   max_depth (int, optional): The maximum depth of crawling. Defaults to 1.

               Example:
                   crawler = WebCrawler()
                   crawler.crawl('https://example.com', max_depth=2)
               """

        parsed_url = urllib.parse.urlparse(start_url)
        self.visited_urls.add(parsed_url.netloc)
        self.queue.append((start_url, depth))

        while self.queue:
            url, current_depth = self.queue.pop(0)
            parsed_url = urllib.parse.urlparse(url)

            if current_depth <= 0 or parsed_url.netloc not in self.visited_urls:
                continue

            self.visited_urls.add(parsed_url.netloc)

            try:
                connection = http.client.HTTPSConnection(parsed_url.netloc)
                connection.request("GET", parsed_url.path)
                response = connection.getresponse()

                if response.status == 200:
                    html_content = response.read().decode("utf-8")
                    self.parse_html(url, html_content)

                    # Extract URLs from the HTML content
                    urls = self.extract_urls(html_content, parsed_url)
                    for new_url in urls:
                        self.queue.append((new_url, current_depth - 1))

                connection.close()

            except Exception as e:
                print(f"Error crawling URL {url}: {str(e)}")

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
