import scrape
from scrape import *


num = 0
while (num < 1):

    vg = scrape("https://www.vg.no", "article", 3, 4)
    printPieChart(countCategories(vg))
    print("Hello World!")
    num += 1
