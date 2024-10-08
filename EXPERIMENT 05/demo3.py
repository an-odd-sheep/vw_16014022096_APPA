from flask import Flask, jsonify, request

app = Flask(__name__)


book_db = [ 
    {'name': 'Bungo Stray Dogs', 'price': 40},
    {'name': 'One piece', 'price': 30},
    {'name': 'Jujustu Kaisen', 'price': 70},
    {'name': 'Naruto', 'price': 60}
]


@app.route('/')
def home():
    return "WELCOME TO vwarrier BOOK-STORE"


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books  on vwarrier book store': book_db})


@app.route('/book/<string:name>', methods=['GET'])
def get_book(name):
    for book in book_db:
        if book['name'].lower() == name.lower():
            return jsonify(book)
    return jsonify({'message': 'Book not found on vwarrier book store'})


@app.route('/book', methods=['POST'])
def create_book():
    new_book = request.get_json()
    book_db.append(new_book)
    return jsonify({'message': 'Book created on vwarrier book store', 'book': new_book})


@app.route('/book/<string:name>', methods=['PUT'])
def update_book(name):
    update_data = request.get_json()
    for book in book_db:
        if book['name'].lower() == name.lower():
            book.update(update_data)
            return jsonify({'message': 'Book updated on vwarrier book store', 'book': book})
    return jsonify({'message': 'Book not found on vwarrier book store'})


@app.route('/book/<string:name>', methods=['DELETE'])
def delete_book(name):
    for book in book_db:
        if book['name'].lower() == name.lower():
            book_db.remove(book)
            return jsonify({'message': 'Book deleted on vwarrier book store'})
    return jsonify({'message': 'Book not found on vwarrier book store'})


app.run(port=5050)
