from flask import request, jsonify, Response, Blueprint

from flaskr import db
from flaskr.models import Book


routes_blueprint = Blueprint('routes_blueprint', __name__)

# @app.route("/")
@routes_blueprint.route('/')
def hello_world() -> str:
    return "<p>Hello, World!</p>"

# @app.route("/books", methods=["GET", "POST"])
@routes_blueprint.route("/books", methods=["GET", "POST"])
def users() -> Response:
    if request.method == 'GET':
        books = Book.query.all()
        data = [book.as_dict() for book in books]
        return jsonify(data)

    if request.method == 'POST':
        title = request.json['title']
        author = request.json['author']
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return f'<p>Book with title: {title} and author {author} successfully added</p>'