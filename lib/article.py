from lib.db import CURSOR, CONN

class Article:
    def __init__(self, title, content, author_id, magazine_id, id=None):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def save(self):
        CURSOR.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
                       (self.title, self.content, self.author_id, self.magazine_id))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM articles")
        rows = CURSOR.fetchall()
        return [Article(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    def author(self):
        from lib.author import Author
        CURSOR.execute("SELECT * FROM authors WHERE id = ?", (self.author_id,))
        row = CURSOR.fetchone()
        return Author(row[1], row[2], row[0])

    def magazine(self):
        from lib.magazine import Magazine
        CURSOR.execute("SELECT * FROM magazines WHERE id = ?", (self.magazine_id,))
        row = CURSOR.fetchone()
        return Magazine(row[1], row[2], row[0])
