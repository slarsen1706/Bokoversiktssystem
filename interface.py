def ProcessInput(inp, library):
    #Uses a match/case structure for all inputs
    match inp.lower():
        #Prints all commands if the user needs to see them
        case "hjelp":
            print("Mulige kommandoer:\nlån (dersom du vil låne en bok)\nreturner (dersom du skal returnere en bok)\nsøk (dersom du skal søke på en bok)\nliste (gir deg en liste over alle bøkene)\npopulære (gir den en liste sortert på antall ganer en bok er lånt)\nlukk (lagrer dataene og lukker programmet)")
        #Borrows a book
        case "lån":
            pass
        #Returns a book
        case "returner":
            pass
        #Search for a book
        case "søk":
            #Another input loop since more inputs are required with correct formatting
            while True:
                #Choosing search method and using another match/case to run correct code
                inp = input("Hvordan ønsker du å søke? (isbn, navn, forfatter, avbryt)\n>>>")
                match inp.lower():
                    #Every case needs an input for seaching and uses that input in the search function
                    #Should the user input a faulty input, they get a retry and can also cancel the command
                    case "isbn":
                        inp = input("ISBN:")
                        result = library.SearchISBN(inp)
                        if result != None:
                            print(library.FormatBooks([result]))
                        else:
                            print("Ingen bok/bøker funnet")
                        return
                    
                    case "navn":
                        inp = input("Navn:")
                        result = library.SearchName(inp)
                        if result != []:
                            print(library.FormatBooks(result))
                        else:
                            print("Ingen bok/bøker funnet")
                        return
                    
                    case "forfatter":
                        inp = input("Forfatter:")
                        result = library.SearchAuthor(inp)
                        if result != []:
                            print(library.FormatBooks(result))
                        else:
                            print("Ingen bok/bøker funnet")
                        return
                        
                    case "avbryt":
                        return
                    case _:
                        print("Kommandoen er ugyldig, om du vil avbryte søkingen, skriv 'avbryt'\n")
                
        case "liste":
            print(library.FormatBooks(library.lib))

        case "populære":
            pass
        
        case "lukk":
            exit()
            
        case _:
            print("Kommandoen er ugyldig, ønsker du å se oversikt over alle kommandoene skriv 'hjelp'")