import dateutil.parser
from flask import make_response, request
from flask_restplus import Model, Resource, fields, marshal_with, reqparse

from app import api, engine
from database.transactions import insert_tables

transaction_model = api.model('Slot game transaction model',
                              {'stamp': fields.DateTime(required=True),
                               'game_id': fields.Integer(required=True),
                               'round_id': fields.Integer(required=True),
                               'amount': fields.Integer(required=True)
                               })

db_conn = engine.connect()


class EpTransaction(Resource):
    @api.expect(transaction_model, validate=True)
    @api.param('Action', 'win or bet')
    def post(self, action):
        if action not in ['win', 'bet']:
            return {'error':
                    'Wrong action url parameter. Can be only win or bet.'}, 400

        data = request.json

        try:
            yourdate = dateutil.parser.parse(data['stamp'])
        except Exception as exc:
            return {'error': 'Unknown stamp format.'}

        data.update({'type': action})
        if insert_tables(db_conn, data):
            return data
        else:
            return {'error': 'Unable to process new data.'}, 500
