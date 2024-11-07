import mysql.connector
import os

from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if "db" not in g or not g.db.is_connected():
        # connect to the database
        g.db = mysql.connector.connect(
            host=current_app.config["MYSQL_DATABASE_HOST"],
            user=current_app.config["MYSQL_DATABASE_USER"],
            passwd=current_app.config["MYSQL_DATABASE_PASSWORD"],
            db=current_app.config["MYSQL_DATABASE_DB"],
            ssl_verify_identity=False,
            ssl_ca='/data/ca.pem',
            ssl_cert='/data/client-cert.pem',
            ssl_key='/data/client-key.pem'
        )

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        # close the database
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)

