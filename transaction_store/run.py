# -*- coding: utf-8 -*-
from app import api, app
from endpoints import EpTransaction

api.add_resource(EpTransaction, '/api/slot/transactions/<action>')
# api.add_resource(TransactionWin, '/api/store/win')

if __name__ == '__main__':
    app.run()
