import json
import os

### Mohamad ###
def GetBookInfo():
    # Collecting book information from the user
    ISBN = input("Enter the ISBN number of the book: ")
    ISBN = ISBN.replace('-', '')
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    genre = input("Enter the genre of the book: ")
    count = input("Enter how many to add: ")
    
    #Return the info as an object, with the isbn as the key
    return {
        ISBN : {
            "name": title,
            "author": author,
            "year": year,
            "genre": genre,
            "count": count
        }
    }
 
def WriteToJSON(info, filename='data.json'):
    # Check if the file already exists
    if os.path.exists(filename):
        # Read existing data
        with open(filename, 'r') as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
 
    # Append the new book information
    data.append(info)
 
    # Write the updated data back to the JSON file
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
 
    print(f"Information has been written to {filename}.")

### Sander ###
def RemoveFromJSON(id, filename='data.json'):
    # Check if the file already exists
    if os.path.exists(filename):
        # Read existing data
        with open(filename, 'r') as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    
    #If the id is in data, remove that id
    if id in data:
        del(data[id])
        
    # Write the updated data back to the JSON file
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def ReplaceJSON(data, filename='data.json'):
    #Write the updated data back to the JSON file, replaces all of the contents in the file
    with open(filename, 'w') as json_file:
        json.dump([data], json_file, indent=4)
     
def ReadJSON(filename="data.json"):
    #if the path does not exist, return an empty array and inform the user
    if not os.path.exists(filename):
        print("JSON path does not exist")
        return []
    #Else return the json contents as a dictionary
    data = json.load(open(filename, 'r'))
    return data[0]
            