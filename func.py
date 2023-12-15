from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer


def get_page(url):
    response = urlopen(url)
    page = BeautifulSoup(
        response.read(),
        parse_only=SoupStrainer('body'),
        features="html.parser"
    )

    return page

print(get_page('https://www.google.com'))