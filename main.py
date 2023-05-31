from scrape import WebCrawler, WebScraper, Scraper
from pre_types import NewsSite, WebStore
# Create an instance of WebCrawler and WebScraper
crawler = WebCrawler()
scraper = WebScraper()

# Create a NewsSite object for example.com
example_news_site = NewsSite("Example News Site", "https://vg.no", scraper)
example_news_site.max_depth = 0  # Set the maximum depth

# Create a WebStore object for examplestore.com
example_web_store = WebStore("Example Web Store", "https://examplestore.com", scraper)
example_web_store.max_depth = 0  # Set the maximum depth

# Define the URLs to start crawling
start_urls = ["https://vg.no", "https://examplestore.com"]

# Crawl and scrape the websites
for url in start_urls:
    if url.startswith("https://vg.no"):
        crawler.crawl(url, example_news_site.max_depth)

    elif url.startswith("https://examplestore.com"):
        crawler.crawl(url, example_web_store.max_depth)

# Scrape the articles and print
example_news_site.scrape_articles(selector=".article")
for article in example_news_site.articles:
    print(f"Article: {article.name}\nURL: {article.url}")

# Scrape the products and print
example_web_store.scrape_products(selector=".product")
for product in example_web_store.products:
    print(f"Product: {product.name}\nURL: {product.url}")