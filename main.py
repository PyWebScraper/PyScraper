import export
from counting import count_categories
from printing import print_pie_chart
from sort import *
from scrape import *


num = 0
while (num < 1):

    vg = scrape("https://www.vg.no", "article", 3, 4, meta_data_class="tracking-data")
    pie_chart = print_pie_chart(count_categories(vg), png=True, pdf=False, filename="foo")
    sort_list_of_objects(vg, 'title')
    print("Hello World!")
    num += 1
