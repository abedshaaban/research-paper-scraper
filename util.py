class Article:
    def __init__(self, title, abstract, authors, citations_number, year, link):
        
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.citations_number = citations_number
        self.year = year
        self.link = link

    def to_json(self):

        return {
            "title": self.title,
            "abstract": self.abstract,
            "authors": self.authors,
            "citations_number": self.citations_number,
            "year": self.year,
            "link": self.link,
        }


letter = Article('aboudi', 'long text', 'Mosbah', 4, 20016, "asdfghjkl")

print(letter.to_json())

