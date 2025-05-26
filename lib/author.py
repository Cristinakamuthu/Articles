# lib/author.py

from lib.db import CURSOR, CONN

class Author:
    def __init__(self, name):
        self.name = name

    def save(self):
        CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        CONN.commit()
