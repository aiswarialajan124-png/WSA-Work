import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

# Get all books
def readbooks():
    response = requests.get(URL)
    return response.json()

# Get one book by ID
def readbook(id):
    getURL = URL +"/" + str(id)
    response = requests.get(getURL)
    return response.json()
 
# Create a new book
def createbook(book):
    response = requests.post(URL, json=book)
    return response.json()

# Update a book
def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

# Delete a book
def deletebook(id):
    deleteurl = URL + "/" +str(id)
    response = requests.delete(deleteurl)
    return response.json()

# Testing code
if __name__ == "__main__":
    print("All books: ")
    print(readbooks())

    print("\nBook with ID 1: ")
    books = readbooks()
    first_id = books[0]["id"]
    print(readbook(first_id))
    