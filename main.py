import export
from counting import count_categories
from printing import print_pie_chart
from sort import *
from scrape import *


num = 0
while (num < 1):
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
    num += 1
