from scrape import ElementSelector, WebScraper


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
    def pretty_print_html(url, indent_size=4, initial_indent=0):
        """Pretty print the HTML content of the web page.

               Args:
                   indent_size (int, optional): The size of the indentation. Defaults to 4.

               Example:
                   page = WebPage(url='https://example.com', html_content='<html>...</html>')
                   page.pretty_print_html()
               """

        result = ""
        html_content = WebScraper.scrape(url)

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

    def scrape_content(self, scraper):
        """Scrapes the content of the article."""
        html_content = self.scraper.scrape(self.url, 'html')

class WebStore(WebPage):
    """Represents a web store."""
    def __init__(self, name, url, scraper):
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
        super().__init__(name, url, scraper)
        self.products = []

    def scrape_products(self, selector):
        """Scrapes products from the web store based on the provided selector.

               Args:
                   selector (str): The selector to identify product elements.

               Example:
                   web_store = WebStore(name='Komplett', url='https://www.komplett.no', html_content='<html>...</html>', scraper=scraper)
                   web_store.scrape_products(selector='.product')
               """
        product_elements = ElementSelector.extract_elements_by_css_selector(self.html_content, selector)
        self.products = [Product(element) for element in product_elements]

class Product(WebPage):
    """Represents a product."""
    def __init__(self, name, url, html_content, scraper):
        """Initialize a Product object.

               Args:
                   name (str): The name of the product.
                   url (str): The URL of the product.
                   html_content (str): The HTML content of the product.
                   scraper (WebScraper): The web scraper instance.

               Example:
                   product = Product(name='Product 1', url='https://www.example.com/product1', html_content='<html>...</html>', scraper=scraper)
               """
        super().__init__(url, html_content, name, scraper)
        self.description = ""

    def scrape_description(self, html_content):
        """Scrapes the description of the product.

        Args:
            html_content (str): The HTML content of the product page.

        Example:
            product = Product(name='Product 1', url='https://www.example.com/product1', html_content='<html>...</html>', scraper=scraper)
            product.scrape_description(html_content)
        """
        description_elements = ElementSelector.extract_elements(html_content,
                                                                selector='//div[@class="product-description"]')
        if description_elements:
            self.description = ' '.join(element.text.strip() for element in description_elements)
