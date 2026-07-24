import sqlite3
import os

DATABASE = os.path.join("database", "blackshield.db")


def connect():
    return sqlite3.connect(DATABASE)
