# -*- coding: utf-8 -*-
from database.models import metadata
from flask.cli import AppGroup
from app import app
from app import engine
import click

database = AppGroup('db')
conn = engine.connect()


@database.command('create')
def create_tables():
    metadata.create_all(engine)


@database.command('drop')
def drop_tables():
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


@database.command('reinit')
@click.pass_context
def recreate_db(ctx):
    ctx.invoke(drop_tables)
    ctx.invoke(create_tables)


if __name__ == '__main__':
    # python manage.py db
    app.cli.add_command(database)
    app.cli()
