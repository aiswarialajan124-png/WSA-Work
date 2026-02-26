from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

# GET all books
@app.route('/books', methods=['GET'])
def getall():
    return "Get all"

# GET book by id
@app.route('/books/<int:id>', methods=['GET'])
def findById(id):
    return f"find by id {id}"

# CREATE book
@app.route('/books', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    return f"create {request.json}"

# UPDATE book
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    if not request.json:
        abort(400)
    return f"update {id} {request.json}"

# DELETE book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == "__main__":
    app.run(debug=True)