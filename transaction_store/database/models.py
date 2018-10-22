from sqlalchemy import (Column, DateTime, ForeignKey, Integer, MetaData,
                        String, Table)

metadata = MetaData()

games_table = Table('games', metadata,
                    Column('id', String, primary_key=True, unique=True)
                    )
rounds_table = Table('rounds', metadata,
                     Column('id', Integer, primary_key=True, unique=True),
                     Column('game_id', None, ForeignKey('games.id'))
                     )
actions_table = Table('actions', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('round_id', None, ForeignKey('rounds.id')),
                      Column('stamp', DateTime, nullable=False),
                      Column('type', String(3), nullable=False),
                      Column('amount', Integer)
                      )