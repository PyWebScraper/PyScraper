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

"""
def pretty_print_html(html_content, indent_size=4, initial_indent=0):
    result = ""

    # Convert bytes to string
    decoded_content = html_content.decode('utf-8')

    for char in decoded_content:
        if char == '<':
            result += "\n" + " " * (indent_size * initial_indent) + char
            initial_indent += 1
        elif char == '>':
            result += char
            if initial_indent > 0:
                initial_indent -= 1
        else:
            result += char

    print(result)


def scrape2(url, article_class, int_where_in_url_is_category,
           int_where_in_url_is_sub_category, meta_data_class=None,
           change_key='changes', published_key='firstPublished', updated_key='updated',
           word_count_key='wordCount'):
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
                    category = url_parts[int_where_in_url_is_category]
                except:
                    category = None
                try:
                    sub_category = url_parts[int_where_in_url_is_sub_category]
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

                if script_tag is not None:
                    meta_data = json.loads(script_tag.text)
                    changes_data = meta_data.get(change_key)
                    if changes_data is not None:
                        date_published = changes_data.get(published_key)
                        date_updated = changes_data.get(updated_key)
                        if date_published is not None:
                            date_published = date_published.rstrip('Z')
                            datetime_raw = datetime.fromisoformat(date_published)
                            date_published = datetime_raw.date()
                            time_published = datetime_raw.time()
                        if date_updated is not None:
                            date_updated = date_updated.rstrip('Z')
                            datetime_raw = datetime.fromisoformat(date_updated)
                            date_updated = datetime_raw.date()
                            time_updated = datetime_raw.time()
                    else:
                        date_published = None
                        date_updated = None
                    word_count = meta_data.get(word_count_key)
                else:
                    date_published = None
                    word_count = None
                    time_published = None
                    time_updated = None
                    date_updated = None


            articles.append(Article(title=title, date_published=date_published, time_published=time_published,
                                    date_updated=date_updated, time_updated=time_updated, word_count=word_count,
                                    url=article_url, category=category, sub_category=sub_category))

            #articles.append(Article(category, sub_category, title, date, content))

    # If the request was not successful, raise an exception
    else:
        raise Exception('Request failed with status code {}'.format(response.status_code))

    for article in articles:
        print(article)
    return articles


def themeify(url, int_where_in_url_is_category, int_where_in_url_is_sub_category):

    parts = url.split('/')
    category = parts[int_where_in_url_is_category]
    sub_category = parts[int_where_in_url_is_sub_category]
    return category, sub_category


"""