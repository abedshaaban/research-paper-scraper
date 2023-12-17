class Article:
    def __init__(self, title, abstract, authors, citations_number, year, link, pdf_link):

        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.citations_number = citations_number
        self.year = year
        self.link = link
        self.pdf_link = pdf_link

    def to_json(self):

        return {
            "title": self.title,
            "abstract": self.abstract,
            "authors": self.authors,
            "citations_number": self.citations_number,
            "year": self.year,
            "link": self.link,
            "pdf": self.pdf_link,
        }
