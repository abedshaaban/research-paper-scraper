from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, SoupStrainer


def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.72 Safari/537.36'}

    req = Request(url, headers=headers)

    try:
        response = urlopen(req)
    except Exception as e:
        print(f"An error occurred: {e}")

    page = BeautifulSoup(
        response.read(),
        parse_only=SoupStrainer('body'),
        features="html.parser"
    )

    return page


page = get_page('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=mlp&oq=')


articles = page.find_all('div', class_='gs_or')
article_div = [link for link in articles]

for article in articles:
    # get title
    h3_element = article.find('h3', class_='gs_rt')
    title = h3_element.a.text

    # get authors
    author_a = article.find_all('div', class_='gs_a')
    author = [author_div.text.strip() for author_div in author_a]
    authors = author[0].replace("\xa0", '').split("-")
    authors.pop()
    authors = authors[0].split(",")

    # get abstract
    abstract_div = article.find('div', class_='gs_rs')
    abstract = abstract_div.text

    # get link
    link = h3_element.a['href']

    # get pdf link
    pdf_div = article.find('div', class_='gs_or_ggsm')
    pdf_link = ''

    if pdf_div is not None:
        pdf_link = pdf_div.a['href']

    # citation number
    citation_div = article.find('div', class_='gs_flb')
    citation_list = [link.text for link in citation_div]
    citation_number = citation_number[4].split(" ")[2]

    # print(title)
    # print(authors)
    # print(abstract)
    # print(link)
    # print(pdf_link)
    # print(citation_number)
    print("-" * 20)
