import pytest
from unittest.mock import MagicMock
from pre_types import *


@pytest.fixture
def scraper_mock():
    return MagicMock()


@pytest.mark.parametrize(
    "class_type, attrs",
    [
        (WebPage, {"name": "Example Page", "url": "https://example.com", "html_content": "<html>...</html>",
                   "attr1": "value1", "attr2": "value2"}),
        (NewsSite, {"name": "Example News Site", "url": "https://example.com", "scraper": scraper_mock,
                    "attr1": "value1", "attr2": "value2"}),
        (Article, {"name": "Example Article", "url": "https://example.com/article", "scraper": scraper_mock,
                   "attr1": "value1", "attr2": "value2", "html_content": "<html>...</html>"}),
        (WebStore, {"name": "Example Web Store", "url": "https://example.com", "scraper": scraper_mock,
                    "attr1": "value1", "attr2": "value2"}),
    ]
)
def test_classes(class_type, attrs):
    obj = class_type(**attrs)

    for attr_name, attr_value in attrs.items():
        assert getattr(obj, attr_name) == attr_value


def test_web_page_pretty_print_html(scraper_mock, capsys):
    html_content = "<html>...</html>"
    page = WebPage(name="Example Page", url="https://example.com", html_content=html_content)

    # Capture the print output for assertion
    with capsys.disabled():
        page.pretty_print_html(html_content)  # Modify or add assertions for the print output if needed


def test_news_site_scrape_articles(scraper_mock):
    selector = ".article"
    news_site = NewsSite(name="Example News Site", url="https://example.com", scraper=scraper_mock)

    # Mock the scrape method to return sample HTML content
    scraper_mock.scrape.return_value = "<html><div class='article'>Article 1</div><div class='article'>Article 2</div></html>"

    news_site.scrape_articles(selector)

    # Add assertions for the scraped articles
    assert len(news_site.articles) == 2
    assert news_site.articles[0].name == "Article"
    assert news_site.articles[0].url == "https://example.com"
    assert news_site.articles[0].scraper == scraper_mock
    # Add more assertions if needed


def test_article_pretty_print_html(scraper_mock, capsys):
    html_content = "<html>...</html>"
    article = Article(name="Example Article", url="https://example.com/article", scraper=scraper_mock, html_content=html_content)

    # Capture the print output for assertion
    with capsys.disabled():
        article.pretty_print_html(html_content)  # Modify or add assertions for the print output if needed


def test_web_store_scrape_products(scraper_mock):
    selector = ".product-item"
    web_store = WebStore(name="Example Web Store", url="https://example.com", scraper=scraper_mock)

    # Mock the scrape method to return sample HTML content
    scraper_mock.scrape.return_value = "<html><div class='product-item'>Product 1</div><div class='product-item'>Product 2</div></html>"

    web_store.scrape_products(selector)

    # Add assertions
    assert len(web_store.products) == 2
    assert web_store.products[0].name == "Product"
    assert web_store.products[0].url == "https://example.com"
    assert web_store.products[0].scraper == scraper_mock
    # Add more assertions if needed
