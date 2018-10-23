# game-transaction-store

- python3.6
- Init db by `manage.py db create`
- Start from `run.py`
- wsgi not included

### Notes
Two possible endpoints, `/api/slot/transactions/<action>` where `<action>` is `win` or `bet`.
Accepted json schema is in swagger (`localhost:5000`).
I've changed game_id value to `int` because it's way safer and easier to parse.
