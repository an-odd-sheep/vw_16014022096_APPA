from flask import Flask, jsonify, request

app = Flask(__name__)

book_db = [
    {
    'name':'harry potter',
    'price': 40
    },
    {
    'name':'lord of the rings',
    'price': 30
    }
]

@app.route('/')
def home():
    return "HELLO HOME"

@app.route('/books')
def books():
    return jsonify({'books': book_db})

@app.route('/book/<string:name>')
def get_book(name):
    for book in book_db:
        if book['name'] == name:
            return jsonify(book)
        return jsonify({'message': 'book not found'})
    
@app.route('/book', methods=['POST'])
def create_book():
    body_data = request.get_json()
    book_db.append(body_data)
    return jsonify({'message': 'book created'})

app.run(port=5050)

