from lib.db import CURSOR, CONN

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        CURSOR.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM magazines")
        rows = CURSOR.fetchall()
        return [Magazine(row[1], row[2], row[0]) for row in rows]

    def articles(self):
        from lib.article import Article
        CURSOR.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        rows = CURSOR.fetchall()
        return [Article(row[1], row[2], row[3], row[4], row[0]) for row in rows]

    def contributors(self):
        from lib.author import Author
        CURSOR.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON ar.author_id = a.id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        rows = CURSOR.fetchall()
        return [Author(row[1], row[2], row[0]) for row in rows]
