class Library(object):
    def __init__(self, books={}):
        # Books er strukturert som ett object, der key er ISBN og value er enda ett objekt {name, author, count}
        self.lib = books
        self.borrowed = {}
        self.borrowedCount = {}
    
    #Since no two books can have the same ISBN, only one book needs to be returned
    def SearchISBN(self, isbn):
        book = self.lib[isbn]
        return book if book != None else "Ingen bok funnet"
    
    #Goes over all books and makes a collection of books with the same name (if theres duplicates)
    def SearchName(self, name):
        books = []
        for isbn in self.lib:
            if self.lib[isbn]['name'].lower() == name.lower():
                books.append(isbn)
        return books
    
    #Goes over all books and makes a collection of books by the same author
    def SearchAuthor(self, author):
        books = []
        for isbn in self.lib:
            if self.lib[isbn]['author'].lower() == author.lower():
                books.append(isbn)
        return books
    
    #Formats books so it is easier to read when printed to console
    def FormatBooks(self, books):
        fmt = ""
        for isbn in books:
            book = self.lib[isbn]
            fmt += f"'{book['name']}' by \x1B[3m{book['author']}\x1B[0m | ISBN: {isbn} | Vi har {book['count']}\n"
        return fmt
            