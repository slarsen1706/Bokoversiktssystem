from book import Book
from library import Library
from interface import *

#This will be replaced with a JSON file reader/writer
startingBooks = {
    	"9780765326355" : {
            "name" : "The Way of Kings",
            "author" : "Brandon Sanderson",
            "count" : 2,
            "year"  : 2010,
            "genre" : "Epic fantasy"
        },
     
        "0345539788" : {
            "name" : "Red Rising",
            "author" : "Pierce Brown",
            "count" : 1,
            "year"  : 2014,
            "genre" : "Science fiction"
        },
}

library = Library(startingBooks)
ProcessInput("hjelp", library)

#The console loop
while True:
    inp = input("\033[93m>>>\033[0m")
    ProcessInput(inp, library)