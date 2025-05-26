from lib.db import CURSOR, CONN
from lib.article import Article

class Author:
    all = []

    def __init__(self, name, genre, id=None):
        self.id = id
        self.name = name
        self.genre = genre
        Author.all.append(self)

    def save(self):
        CURSOR.execute("INSERT INTO authors (name, genre) VALUES (?, ?)", (self.name, self.genre))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM authors")
        rows = CURSOR.fetchall()
        return [Author(row[1], row[2], row[0]) for row in rows]

    def articles(self):
        CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = CURSOR.fetchall()
        from lib.article import Article
        return [Article(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    def magazines(self):
        CURSOR.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = CURSOR.fetchall()
        from lib.magazine import Magazine
        return [Magazine(row[1], row[2], row[0]) for row in rows]
