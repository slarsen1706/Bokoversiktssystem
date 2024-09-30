from library import Library
from interface import *
from jsonModule import *

#Initializes the library class using the json files
library = Library(books=ReadJSON("Høstsemester/Bokoversiktssystem/books.json"), loaned=ReadJSON("Høstsemester/Bokoversiktssystem/loaned.json"))

#Prints a library ascii art
print('\033[93m       .--.           .---.        .-.              \033[0m')
print('\033[93m   .---|--|   .-.     | A |  .---. |~|    .--.      \033[0m')
print('\033[93m.--|===|Ch|---|_|--.__| S |--|:::| |~|-==-|==|---.  \033[0m')
print('\033[93m|%%|NT2|oc|===| |~~|%%| C |--|   |_|~|CATS|  |___|-.\033[0m')
print('\033[93m|  |   |ah|===| |==|  | I |  |:::|=| |    |GB|---|=|\033[0m')
print('\033[93m|  |   |ol|   |_|__|  | I |__|   | | |    |  |___| |\033[0m')
print('\033[93m|~~|===|--|===|~|~~|%%|~~~|--|:::|=|~|----|==|---|=|\033[0m')
print("\033[93m^--^---'--^---^-^--^--^---'--^---^-^-^-==-^--^---^-'\033[0m")

#Prints a list of commands
ProcessInput("hjelp", library)

#The console loop
while True:
    #Get the users input and process it
    inp = input("\033[93m>\033[0m")
    ProcessInput(inp, library, jsonPath='Høstsemester/Bokoversiktssystem/books.json')