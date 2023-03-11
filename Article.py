class Article:
    def __init__(self, title, category, sub_category, url, date_published, date_updated=None, most_repeated_phrase=None):
        self.title = title
        self.category = category
        self.sub_category = sub_category
        self.url = url
        self.date_published = date_published
        self.date_updated = date_updated
        self.most_repeated_phrase = most_repeated_phrase
