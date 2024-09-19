from library import Library
from interface import *
from jsonModule import *

#Initializes the library class using the json files
library = Library(books=ReadJSON("Høstsemester/Bokoversiktssystem/books.json"), loaned=ReadJSON("Høstsemester/Bokoversiktssystem/loaned.json"))

#Prints a list of commands
ProcessInput("hjelp", library)

#The console loop
while True:
    #Get the users input and process it
    inp = input("\033[93m>\033[0m")
    ProcessInput(inp, library, jsonPath='Høstsemester/Bokoversiktssystem/books.json')