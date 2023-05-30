from scrape import ElementSelector


class WebPage:
    """Represents a web page."""
    def __init__(self, url, html_content, name, **kwargs):
        """Initialize a WebPage object.

                Args:
                    url (str): The URL of the web page.
                    html_content (str): The HTML content of the web page.
                    name (str, optional): The name of the web page. Defaults to an empty string.
                    sub_urls (list, optional): A list of sub-URLs associated with the web page. Defaults to None.
                    **kwargs: Additional user-defined attributes.

                Example:
                    page = WebPage(url='https://example.com', html_content='<html>...</html>', name='Example Page')
                """

        self.url = url
        self.html_content = html_content
        self.name = name

        # Set user-defined attributes
        for attr_name, attr_value in kwargs.items():
            setattr(self, attr_name, attr_value)


    @staticmethod
    def pretty_print_html(html_content, indent_size=4, initial_indent=0):
        """Pretty print the HTML content of the web page.

               Args:
                   indent_size (int, optional): The size of the indentation. Defaults to 4.

               Example:
                   page = WebPage(url='https://example.com', html_content='<html>...</html>')
                   page.pretty_print_html()
               """

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


    def print_name(self):
        print("Page Name:", self.name)

    def print_url(self):
        print("Page URL:", self.url)

    def print_html(self):
        print("Page HTML:")
        self.pretty_print_html(self.html_content)


class NewsSite(WebPage):
    """Represents a news site."""
    def __init__(self, name, url, scraper):
        """Initialize a NewsSite object.

            Args:
                url (str): The URL of the news site.
                html_content (str): The HTML content of the news site.
                name (str, optional): The name of the news site. Defaults to an empty string.
                sub_urls (list, optional): A list of sub-URLs associated with the news site. Defaults to None.
                latest_articles (list, optional): A list of latest articles on the news site. Defaults to None.
                **kwargs: Additional user-defined attributes.

            Example:
                news_site = NewsSite(url='https://example.com', html_content='<html>...</html>', name='Example News Site')
        """
        super().__init__(name, url, scraper)
        self.articles = []




 def scrape_articles(self, selector):
        """Scrapes articles from the news site based on the provided selector."""
        html_content = self.scraper.scrape(self.url, 'html')
        article_elements = ElementSelector.extract_elements_by_css_selector(html_content, selector)
        self.articles = [Article(element) for element in article_elements]


class Article(WebPage):
    def __init__(self, name, url, scraper):
        super().__init__(name, url, scraper)
        self.content = ""

    def scrape_content(self):
        """Scrapes the content of the article."""
        html_content = self.scraper.scrape(self.url, 'html')

class WebStore(WebPage):
    """Represents a web store."""
    def __init__(self, url, html_content, name):
        """Initialize a WebStore object.

               Args:
                   url (str): The URL of the web store.
                   html_content (str): The HTML content of the web store.
                   name (str, optional): The name of the web store. Defaults to an empty string.
                   sub_urls (list, optional): A list of sub-URLs associated with the web store. Defaults to None.
                   products (list, optional): A list of products available in the web store. Defaults to None.
                   **kwargs: Additional user-defined attributes.

               Example:
                   web_store = WebStore(url='https://example.com', html_content='<html>...</html>', name='Example Web Store')
               """
        super().__init__(url, html_content)
        self.name = name

    def print_name(self):
        print("Store Name:", self.name)