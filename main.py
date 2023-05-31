from scrape import WebCrawler, WebScraper, Scraper
from Types import NewsSite, WebStore


num = 0
while (num < 1):

    # Create an instance of WebCrawler and WebScraper
    crawler = WebCrawler()
    scraper = WebScraper()

    # Create a NewsSite object for vg.no
    vg_news_site = NewsSite("VG", "https://www.vg.no", scraper)
    vg_news_site.scraper = scraper
    vg_news_site.max_depth = 1  # Set the maximum depth

    # Create a WebStore object for komplett.no
    komplett_web_store = WebStore("Komplett", "https://www.komplett.no", scraper)
    komplett_web_store.max_depth = 1  # Set the maximum depth

    # Define the URLs to start crawling
    start_urls = ["https://www.vg.no", "https://www.komplett.no"]

    # Crawl and scrape the websites
    for url in start_urls:
        if url.startswith("https://www.vg.no"):
            #crawler.crawl(url, vg_news_site.max_depth)
            vg_news_site.scrape_articles('.article')
        elif url.startswith("https://www.komplett.no"):
            crawler.crawl(url, komplett_web_store.max_depth)
            komplett_web_store.scrape_products()

    # Access the scraped data
    print("Latest articles from VG:")
    for article in vg_news_site.articles:
        print(article.title)

    print("\nLatest products from Komplett:")
    for product in komplett_web_store.products:
        print(product.title)

    num += 1
    """
    url = 'https://www.vg.no'
    field_mappings = {
        'title': {
            'type': 'html',
            'tag': 'a',
            'attributes': {'class': 'article-contentlink'},
            'sub_selectors': 'h2'
        },
        'date_published': {
            'type': 'html',
            'tag': 'time',
            'attributes': {'class': 'ArticleDate'},
        },
        'author': {
            'type': 'html',
            'tag': 'span',
            'attributes': {'class': 'ArticleAuthor__name'},
        },
        # Add more field mappings as needed
    }

    # Example usage
    scraper = WebScraper()

    # Scrape HTML content
    html_content = scraper.scrape('https://www.example.com', data_type='html')

    # Scrape JSON data
    #json_data = scraper.scrape('https://api.example.com/data', data_type='json')
    #print(json_data)

    #vg = scrape2("https://www.vg.no", "article", 3, 4, meta_data_class="tracking-data")
    #pie_chart = print_pie_chart(count_categories(vg), png=True, pdf=False, filename="foo")
    #sort_list_of_objects(vg, 'title')
    #print("Hello World!")
    num += 1"""
