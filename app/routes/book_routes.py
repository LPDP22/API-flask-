from flask import Blueprint
from app.controllers import book_controller

book_bp = Blueprint("books", __name__)

book.bp.route("/books", methods=["POST"])(book_controller.add_book)
