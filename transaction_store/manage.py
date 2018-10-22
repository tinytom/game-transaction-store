from database.models import metadata
from flask.cli import AppGroup
from app import app
from app import engine

database = AppGroup('db')
conn = engine.connect()


@database.command('create')
def create_tables():
    metadata.create_all(engine)


@database.command('drop')
def drop_tables():
    metadata.drop_all(engine)


@database.command('reinit')
def recreate_db():
    if 'postgresql' in str(conn.engine.url):
        # postgres DROP ALL CASCADE
        tables = conn.execute(
            "SELECT table_name FROM information_schema.tables "
            "WHERE table_schema='public'")

        for table in tables:
            conn.execute(f"DROP TABLE IF EXISTS {table[0]} CASCADE")
        tables.close()
    else:
        metadata.drop_all(engine)

    metadata.create_all(engine)


if __name__ == '__main__':
    app.cli.add_command(database)
    app.cli()
