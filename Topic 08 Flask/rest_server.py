# Data Representation - Winter 2022
# Flask Application Server
# Author: Ross Downey
# Lecturer: Andrew Beatty

from flask import Flask,url_for, request, abort, jsonify # import necessary functions from flask

# set app to be used
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# array of books
books=[
    {"id": 1, "Title": "Python for Dummies", "Author": "Joe Bloggs", "Price": 13},
    {"id": 2, "Title": "Python Intermediate", "Author": "Jane Doe", "Price": 17},
    {"id": 3, "Title": "Python Expert", "Author": "Paddy Reilly", "Price": 20}
]
# global variable needed for create function
nextId = 4

# Test getAll function using: curl http://127.0.0.1:5000/books
@app.route('/books')
def getAll():
    return jsonify(books)

# Test findById function using: curl http://127.0.0.1:5000/books/1 for example
@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter(lambda t : t["id"] == id, books)) # lambda function
    if len(foundBooks) == 0:
        return jsonify({}), 204 # 204 code, no content
    return jsonify(foundBooks[0])


# Test create function using curl -X POST -H "content-type:application/json" -d "{\"Title\": \"Test"\,\"Author"\: \"Test Author\", \"Price\": 999}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400) # 400 code, bad request if not in json format
    book = {
        "id": nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"]  # requesting variables as json
    }
    books.append(book)
    nextId += 1 # append to books array and increment global variable to give next id number
    return jsonify(book)


# Test update function using: curl -X PUT -d "{\"Title\":\"Updated\",\"Author\": \"Updated Author\", \"Price\": 666}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter(lambda t: t["id"] == id,books))
    if len(foundBooks) == 0:
        return jsonify({}), 404 # If book not found to update return bad request error code
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price'] # New variables to update with new data

    return jsonify(currentBook)

# Test delete function using: curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404 # same as update, if note there, 404 error code returned
    books.remove(foundBooks[0]) # delete

    return jsonify({"done": True}) # output boolean True if successful

def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug = True) # Main function to be run