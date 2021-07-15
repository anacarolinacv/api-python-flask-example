from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id': 0, 'title': '1984'},
    ['id': 1, 'title': 'O CONTO DA AIA'],
    ['id': 2, 'title': 'Forrest Gump']
]

@api.route('/books')
class BookList(Resource):
    def get(self, ):
        return books_db

    def post(self, ):
        response = api.payload
        books_db.append(response)
        return response, 200