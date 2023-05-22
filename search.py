from printing import pretty_print


def find_articles_with_phrase(list_of_article_objects, phraseToFind):
    hits = []
    for article in range(list_of_article_objects):
        if phraseToFind in list_of_article_objects.text:
            hits.append(article)
    return pretty_print(hits)


def find_articles_with_word(list_of_article_objects, wordToFind):

    hits = []
    for article in range(list_of_article_objects):
        if wordToFind in list_of_article_objects.text:
            hits.append(article)
    return pretty_print(hits)