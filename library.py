class Library(object):
    def __init__(self, books={}):
        # Books er strukturert som ett object, der key er ISBN og value er enda ett objekt {name, author, count}
        self.lib = books
        self.loaned = {}
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
    
    def AddLoaned(self, isbn, name):
        self.loaned.update({isbn, "name" : name})
    
    def LoanBook(self, isbn):
        # Søk etter bok basert på ISBN
        for code in self.lib:
            if code == isbn:  # Sjekk om ISBN matcher
                book = self.lib[code]
                if book['count'] > 0:  # Sjekk om boken er tilgjengelig
                    book['count'] -= 1  # Marker boken som utlånt
                    print(f"Boken '{book['name']}' er nå utlånt.")  # Informer brukeren
                    return True  # Avslutt funksjonen
                else:
                    print(f"Boken '{book['name']}' er allerede utlånt.")  # Hvis boken allerede er utlånt
                    return False # Avslutt funksjonen
        print(f"Ingen bok med ISBN {isbn} funnet.")  # Hvis ingen bok med det oppgitte ISBN finnes
    
    def ReturnBook(self, isbn):
        # Søk etter bok basert på ISBN
        for code in self.lib:
            book = self.lib[code]
            if code == isbn:  # Sjekk om ISBN matcher
                if not isbn in self.loaned:  # Sjekk om boken er utlånt
                    book['count'] += 1   # Marker boken som tilgjengelig igjen
                    print(f"Boken '{book['name']}' er nå returnert.")  # Informer brukeren
                    return  # Avslutt funksjonen
                else:
                    print(f"Boken '{book['name']}' var ikke utlånt.")  # Hvis boken ikke var utlånt
                    return  # Avslutt funksjonen
                
        print(f"Ingen bok med ISBN {isbn} funnet.")  # Hvis ingen bok med det oppgitte ISBN finnes
        
    