from datetime import datetime

from flask import make_response, request
from flask_restplus import Model, Resource, fields, marshal_with, reqparse
from database.transactions import insert_tables
from app import api, engine


transaction_model = api.model('Transaction model',
                              {'stamp': fields.String(required=True),
                               'game_id': fields.String(required=True),
                               'round_id': fields.Integer(required=True),
                               'amount': fields.Integer(required=True)
                               })

db_conn = engine.connect()


class Transaction(Resource):
    @api.expect(transaction_model, validate=True)
    @api.param('Action', 'win or bet')
    def post(self, action):
        if action not in ['win', 'bet']:
            return {'error':
                    'Wrong action url parameter. Can be only win or bet.'}, 400

        data = request.json
        data.update({'type': action})
        if insert_tables(db_conn, data):
            return data
        else:
            return {'error': 'Unable to process new data.'}, 500
