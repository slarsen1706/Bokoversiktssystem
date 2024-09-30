class Library(object):
    def __init__(self, books={}, loaned={}):
        # Books er strukturert som ett object, der key er ISBN og value er enda ett objekt {name, author, count}
        self.lib = books
        self.loaned = loaned
        self.loanedCount = {}
    
    #Since no two books can have the same ISBN, only one book needs to be returned
    def SearchISBN(self, isbn):
        if not isbn in self.lib:
            return None
        book = self.lib[isbn]
        return book
    
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
    def FormatBooks(self, books, index=False):
        fmt = ""
        i = 0
        for isbn in books:
            book = self.lib[isbn]
            pfx = f"{i}: " if index else ""
            fmt += f"{pfx}'\033[1m{book['name']}\033[0m' : {book['genre']} by \x1B[3m{book['author']} ({book['year']})\x1B[0m | ISBN: {isbn} | Vi har {book['count']}\n"
            i += 1
        return fmt
    
    #Adds and removes the loaned boks in the JSON files
    def AddLoaned(self, isbn, name):
        if not isbn in self.loaned:
            self.loaned.update({isbn : [name.lower()]})
        else:
            self.loaned[isbn].append(name.lower())
                    
        if isbn in self.loanedCount:
            self.loanedCount[isbn] += 1
        else:
            self.loanedCount.update({isbn : 1})
            
    def RemoveLoaned(self, isbn, name):
        if len(self.loaned[isbn]) > 1:
            self.loaned[isbn].remove(name)
            return
        del(self.loaned[isbn])          
    
    ##### Noh #####
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
    
    def ReturnBook(self, isbn, name):
        # Søk etter bok basert på ISBN
        for code in self.lib:
            book = self.lib[code]
            if code == isbn:  # Sjekk om ISBN matcher
                if isbn in self.loaned:  # Sjekk om boken er utlånt
                    if name in self.loaned[isbn]:
                        book['count'] += 1   # Marker boken som tilgjengelig igjen
                        print(f"Boken '{book['name']}' er nå returnert.")  # Informer brukeren
                        return True  # Avslutt funksjonen
                    else:
                        print(f"Denne personen har ikke lånt '{book['name']}'")  # Informer brukeren
                        return False
                else:
                    print(f"Boken '{book['name']}' var ikke utlånt.")  # Hvis boken ikke var utlånt
                    return False  # Avslutt funksjonen
                
        print(f"Ingen bok med ISBN {isbn} funnet.")  # Hvis ingen bok med det oppgitte ISBN finnes
        
    