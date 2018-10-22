# -*- coding: utf-8 -*-
from endpoints import Transaction
from app import app, api

api.add_resource(Transaction, '/api/slot/transactions/<action>')
# api.add_resource(TransactionWin, '/api/store/win')

if __name__ == '__main__':
    app.run()
