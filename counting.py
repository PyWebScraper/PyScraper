from matplotlib import pyplot as mpl


def themeify(url,int_Where_In_URL_is_Category, int_Where_in_URL_is_SubCategory,):

    parts = url.split('/')
    category = parts[int_Where_In_URL_is_Category]
    sub_category = parts[int_Where_in_URL_is_SubCategory]
    return category, sub_category


def count_phrases(list_of_article_objects, phraseToCount):
    hits = []
    for article in range(list_of_article_objects):
        if phraseToCount in list_of_article_objects.text:
            hits.append(article)
    return len(hits)


def count_word(list_of_article_objects, wordToCount):

    hits = []
    for article in range(list_of_article_objects):
        if wordToCount in list_of_article_objects.text:
            hits.append(article)
    return len(hits)


def compare_news_websistes(list_of_article_objects, list_of_article_objects_2nd_website, word=None, phrase=None,
                           url_website_1=None, url_website_2=None,
                           metadata_class_url_one=None, metadata_class_url_two=None):

    if phrase is not None:
        website_1_phrase = count_phrases(list_of_article_objects, phrase)
        website_2_phrase = count_phrases(list_of_article_objects_2nd_website, phrase)
        if website_1_phrase > website_2_phrase:
            print(f"The first website has more occurences of the phrase: {phrase} with {website_1_phrase} occurences vs. the other websites: {website_2_phrase}\n")
        elif website_2_phrase > website_1_phrase:
            print(f"The second website has more occurences of the phrase: {phrase} with {website_2_phrase} occurences vs. the other websites: {website_1_phrase}\n")
        elif website_2_phrase == website_1_phrase:
            print(f"Both websites have the same number of occurances of {phrase}, with {website_1_phrase} occurences each\n")

    if word is not None:
        website_1_word = count_phrases(list_of_article_objects, word)
        website_2_word = count_phrases(list_of_article_objects_2nd_website, word)
        if website_1_word > website_2_word:
            print(f"The first website has more occurences of the word: {word} with {website_1_word} occurences vs. the other websites: {website_2_word}\n")
        elif website_2_word > website_1_word:
            print(f"The second website has more occurences of the word: {word} with {website_2_word} occurences vs. the other websites: {website_1_word}\n")
        elif website_2_word == website_1_word:
            print(f"Both websites have the same number of occurances of {word}, with {website_1_word} occurences each\n")

    if url_website_1 and url_website_2 is not None:
        if metadata_class_url_one and metadata_class_url_two is not None:
            website_1_metaData = count_metadata(url_website_1, metadata_class_url_one)
            website_2_metaData = count_metadata(url_website_2, metadata_class_url_two)
            if website_1_metaData > website_2_metaData:
                print(
                    f"The first website has more occurences of metadata with {website_1_metaData} occurences vs. the other websites: {website_2_metaData}\n")
            elif website_2_metaData > website_1_metaData:
                print(
                    f"The second website has more occurences of metadata with {website_2_metaData} occurences vs. the other websites: {website_1_metaData}\n")
            elif website_2_metaData == website_1_metaData:
                print(
                    f"Both websites have the same number of occurances of metadata, with {website_1_metaData} occurences each\n")

    print("The two websites have the following spread of categories: ")
    print(f"The 1st website: {count_categories(list_of_article_objects)}")
    print(f"The 2nd website: {count_categories(list_of_article_objects_2nd_website)}")


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


def sort_list_of_objects(data, sort_param='title', reverse=False):
    sorted_data = sorted(data, key=lambda x: getattr(x, sort_param), reverse=reverse)
    return sorted_data


def compare_html_code(url1, url2):
    #TODO: find diffrences
    #TODO: the function itself
    pass


def count_metadata(webpage, metadata_class):
    #TODO: add logic of the function
    pass


def compare_metadata(page1, page2, metadata_class_website_one, metadata_class_website_two):

    meta_count1 = count_metadata(page1, metadata_class_website_one)
    meta_count2 = count_metadata(page2, metadata_class_website_two)

    if meta_count1 > meta_count2:
        return "Page 1 has more metadata"
    elif meta_count2 > meta_count1:
        return "Page 2 has more metadata"
    else:
        return "Both pages have the same amount of metadata"


def pretty_print(list):
    for item in range(list):
        print(f"{item}\n")


def print_pie_chart(dictionary):

    labels = list(dictionary.keys())
    values = list(dictionary.values())

    mpl.pie(values, labels=labels, autopct='%1.1f%%')
    mpl.axis('equal')

    mpl.show()


def print_pie_chart_from_lists(list_of_labels, list_of_values):
    labels = list(list_of_labels)
    values = list(list_of_values)

    mpl.pie(values, labels=labels, autopct='%1.1f%%')
    mpl.axis('equal')

    mpl.show()