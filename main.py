from counting import count_categories, print_pie_chart
from scrape import *


num = 0
while (num < 1):

    vg = scrape("https://www.vg.no", "article", 3, 4)
    print_pie_chart(count_categories(vg))

    print("Hello World!")
    num += 1
