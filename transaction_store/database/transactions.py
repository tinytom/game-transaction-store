from sqlalchemy.exc import IntegrityError
from sqlalchemy.types import DateTime


def insert_tables(db_conn, data):
    with db_conn.begin():
        try:
            db_conn.execute(
                f"INSERT INTO games ( id ) VALUES ( {data['game_id']} )")
        except IntegrityError:
            # Already in database
            pass

    with db_conn.begin():
        try:
            db_conn.execute(
                "INSERT INTO rounds ( id, game_id ) VALUES "
                f"( {data['round_id']}, {data['game_id']} )")
        except IntegrityError:
            pass

    with db_conn.begin() as trans:
        try:
            db_conn.execute(
                "INSERT INTO actions (round_id, stamp, type, amount) VALUES "
                "( {round_id}, '{stamp}', '{type}', {amount} )".format_map(data)
            )
        except Exception as exc:
            # logger.exception(exc)
            trans.rollback()
            return False
        else:
            trans.commit()
            return True
