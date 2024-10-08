from jsonModule import *

def ProcessInput(inp, library, jsonPath='data.json'):
    #Uses a match/case structure for all inputs
    match inp.lower():
        #Prints all commands if the user can use
        case "hjelp":
            print("\033[96mMulige kommandoer:\033[0m\n\033[92mlån (dersom du vil låne en bok)\nreturner (dersom du skal returnere en bok)\nsøk (dersom du skal søke på en bok)\nliste (gir deg en liste over alle bøkene)\nlegg til (Om du skal legge til en bok)\nlukk (lagrer dataene og lukker programmet)\033[0m")
        #Borrows a book
        case "lån":
            while True:
                #Takes in the user's input
                bookName = input("\033[96mSkriv navn på boken du ønsker å låne\033[0m\n\033[93m>>>\033[0m").lower()
                if bookName == "avbryt":
                    return

                #Search for the book that the user has chosen                
                books = library.SearchName(bookName)
                book = None
                if len(books) == 0:
                    print(f"\033[91mIngen bok med navn {bookName} funnet\033[0m")
                    continue
                if len(books) > 1:
                    #Printer ut en liste med bøkene med samme navn
                    print(library.FormatBooks(books, index=True))
                    
                    #Brukeren skriver inn index til boken de ønsker å velge
                    while True:
                        i = input("\033[96mFant flere bøker med samme navn, hvilke av dem ønsker du å låne (skriv tallet som står foran boka)\033[0m\n\033[93m>>>\033[0m").lower()
                        if i.isnumeric():
                            if int(i) < len(books):
                                book = books[int(i)]
                                break
                            else:
                                print(f"\033[91mIngen bok med index {i}, venligst prøv igjen\033[0m")
                        #Dersom brukeren vil avbryte
                        if i.lower() == "avbryt":
                            return
                else:
                    book = books[0]
                
                name = input("\033[96mHva er ditt fulle navn?\033[0m\n\033[93m>>>\033[0m").lower()
                
                #Låner boka
                if library.LoanBook(book):
                    library.AddLoaned(book, name)
                    ReplaceJSON(library.loaned, filename='Høstsemester/Bokoversiktssystem/loaned.json')
                    ReplaceJSON(library.lib, filename='Høstsemester/Bokoversiktssystem/books.json')
                return            
        #Returns a book
        case "returner":
            #Input loop
            while True:
                bookName = input("\033[96mHvilken bok skal du returere?\033[0m\n\033[93m>>>\033[0m").lower()

                if bookName == "avbryt":
                    return

                #Search for what book the user wants to return
                books = library.SearchName(bookName)
                book = None
                #If there are no books
                if len(books) == 0:
                    print(f"\033[91mIngen bok med navn {bookName} funnet\033[0m")
                    continue
                
                #Dersom det  mer enn en bok med samme navn
                elif len(books) > 1:
                    print(library.FormatBooks(books, index=True))

                    #Input loop
                    while True:
                        i = input("\033[96mFant flere bøker med samme navn, hvilke av dem ønsker du å låne (skriv tallet som står foran boka)\033[0m\n\033[93m>>>\033[0m").lower()
                        #If the input is numeric, choose the index of that book from the books with the same name
                        if i.isnumeric():
                            #If the index is within the range provided
                            if int(i) < len(books):
                                book = books[int(i)]
                                break
                            else:
                                print(f"\033[91mIngen bok med index {i}, venligst prøv igjen\033[91m")
                        if i.lower() == "avbryt":
                            return
                    #If there is only one book
                else:
                    book = books[0]

                name = input("\033[96mHva er ditt fulle navn?\033[0m\n\033[93m>>>\033[0m").lower()

                #Checks if the return is valid and if so, removes the info from loaned.json and adds one to the count in books.json
                if library.ReturnBook(book, name):
                    library.RemoveLoaned(book, name)
                    ReplaceJSON(library.loaned, filename='Høstsemester/Bokoversiktssystem/loaned.json')
                    ReplaceJSON(library.lib, filename='Høstsemester/Bokoversiktssystem/books.json')
                return
        #Search for a book
        case "søk":
            #Another input loop since more inputs are required with correct formatting
            while True:
                #Choosing search method and using another match/case to run correct code
                inp = input("\033[96mHvordan ønsker du å søke? (isbn, navn, forfatter, avbryt)\033[0m\n\033[93m>>>\033[0m")
                match inp.lower():
                    #Every case needs an input for searching and uses that input in the search function
                    #Should the user input a faulty input, they get a retry and can also cancel the command
                    case "isbn":
                        inp = input("\033[93mISBN:\033[0m")
                        result = library.SearchISBN(inp)
                        if result != None:
                            print(library.FormatBooks([result]))
                        else:
                            print("\033[91mIngen bok/bøker funnet\033[0m")
                        return
                    
                    case "navn":
                        inp = input("\033[93mNavn:\033[0m")
                        result = library.SearchName(inp)
                        if result != []:
                            print(library.FormatBooks(result))
                        else:
                            print("\033[91mIngen bok/bøker funnet\033[0m")
                        return
                    
                    case "forfatter":
                        inp = input("\033[93mForfatter:\033[0m")
                        result = library.SearchAuthor(inp)
                        if result != []:
                            print(library.FormatBooks(result))
                        else:
                            print("\033[91mIngen bok/bøker funnet\033[0m")
                        return
                    #If the user wishes to cance and return to the main channel
                    case "avbryt":
                        return
                    #If none of the cases above match, the comand is invalid
                    case _:
                        print("\033[91mKommandoen er ugyldig, om du vil avbryte søkingen, skriv '\033[0m\033[93mavbryt\033[0m\033[91m'\033[0m\n")
        #Prints a list of all books, their isbn, author, genre and count
        case "liste":
            print(library.FormatBooks(library.lib))
        #Adds a book to the library
        case "legg til":
            info = GetBookInfo()
            WriteToJSON(info, filename=jsonPath)
            library.lib = ReadJSON(filename=jsonPath)
        #Closes the program
        case "lukk":
            exit()
        #If the command is not one of the cases above, it is invalid.    
        case _:
            print("\033[91mKommandoen er ugyldig, ønsker du å se oversikt over alle kommandoene skriv 'hjelp'\033[0m")