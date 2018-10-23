# game-transaction-store

- python3.6
- Init db by `manage.py db create`
- Start from `run.py`
- wsgi not included

### Notes
Two possible endpoints, `/api/slot/transactions/<action>` where `<action>` is `win` or `bet`.
Accepted json schema is in swagger (`localhost:5000`).
I've changed `game_id` value to `int` because it's way safer and easier to parse.

### Database
Going with the requests example from the document, because there were requests with same game, round but multiple values of win/bet (and stamp, amount) I derived the database model to be `1 game : N rounds` **and** `1 round : N actions(win/bet, amount, stamp)`.
