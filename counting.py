def count_phrases(list_of_article_objects, phrase_to_count):
    hits = []
    for article in range(list_of_article_objects):
        if phrase_to_count in list_of_article_objects.text:
            hits.append(article)
    return len(hits)


def count_word(list_of_article_objects, word_to_count):

    hits = []
    for article in range(list_of_article_objects):
        if word_to_count in list_of_article_objects.text:
            hits.append(article)
    return len(hits)


def count_categories(list_of_article_objects):

    article_counts = {}
    for article in list_of_article_objects:
        category = article.category
        if category in article_counts:
            article_counts[category] += 1
        else:
            article_counts[category] = 1

    print(article_counts)
    return article_counts


def count_sub_categories(list_of_article_objects):

    article_counts = {}
    for article in list_of_article_objects:
        sub_category = article.sub_category
        if sub_category in article_counts:
            article_counts[sub_category] += 1
        else:
            article_counts[sub_category] = 1

    print(article_counts)
    return article_counts


def count_metadata(webpage, metadata_class):
    #TODO: add logic of the function
    pass


