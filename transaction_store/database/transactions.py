from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.types import DateTime
import traceback


def check_add_new_game(db_conn, game_id):
    try:
        db_conn.execute(
            f"INSERT INTO games (id) VALUES ( '{game_id}' )")
    except IntegrityError:
        # Already in db
        pass


def check_add_new_round(db_conn, round_id, game_id):
    try:
        db_conn.execute(
            "INSERT INTO rounds ( id, game_id ) VALUES "
            f"( '{round_id}', '{game_id}' )")
    except IntegrityError:
        pass

    return True


def add_action(db_conn, data):
    try:
        result = db_conn.execute(
            "INSERT INTO actions (round_id, stamp, type, amount) VALUES "
            "( {round_id}, '{stamp}', '{type}', {amount} )".format_map(data)
        )
    except DataError:
        return False

    return True


def insert_tables(db_conn, data):
    states = [check_add_new_game(db_conn, data['game_id']),
              check_add_new_round(db_conn, data['round_id'], data['game_id']),
              add_action(db_conn, data)]
    if all(states):
        return True
    else:
        # logger.error(states)
        return False
