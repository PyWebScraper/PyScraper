import Article
from scrape import *

num = 0
while (num < 1):
    links, text = scrape("https://www.vg.no")
    print(links)
    print(text)
    print("Hello World!")
    num += 1
