import scrape
from scrape import WebCrawler, WebScraper, Scraper
from pre_types import NewsSite

# Create an instance of WebCrawler and WebScraper
crawler = WebCrawler()
scraper = WebScraper()

# Create a NewsSite object for vg.no
vg_news_site = NewsSite("VG", "https://vg.no", scraper)
vg_news_site.max_depth = 1  # Set the maximum depth

# Define the URLs to start crawling
start_urls = ["https://vg.no"]

# Crawl and scrape the website
for url in start_urls:
    if url.startswith("https://vg.no"):
        crawler.crawl(url, vg_news_site.max_depth)

# Scrape the articles using XPath and print
html_content = scraper.scrape(vg_news_site.url, 'html')
article_elements = scrape.ElementSelector.extract_elements_by_xpath(html_content, "//article")
for article_element in article_elements:
    article_url = Scraper.extract_attribute(article_element, "href")
    article_name = Scraper.extract_text(article_element)
    print(f"Article: {article_name}\nURL: {article_url}")
