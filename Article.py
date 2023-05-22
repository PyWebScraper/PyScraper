class Article:
    def __init__(self, title="Unknown", category="unidentified", sub_category=None, url=None,
                 date_published=None, time_published=None,
                 date_updated=None, time_updated=None, word_count=None, most_repeated_phrase=None,
                 article_text=None):
        self.title = title
        self.category = category
        self.sub_category = sub_category
        self.url = url
        self.date_published = date_published
        self.time_published = time_published
        self.date_updated = date_updated
        self.time_updated = time_updated
        self.word_count = word_count
        self.most_repeated_phrase = most_repeated_phrase
        self.article_text = article_text

    def __str__(self):
        return f"Title: {self.title}\n" \
               f"Date Published: {self.date_published}\n" \
               f"Time Published: {self.time_published}\n" \
               f"Date Updated: {self.date_updated}\n" \
               f"Time Updated: {self.time_updated}\n" \
               f"Word Count: {self.word_count}\n" \
               f"URL: {self.url}\n" \
               f"Category: {self.category}\n" \
               f"Sub Category: {self.sub_category}\n"