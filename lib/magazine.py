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
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        if row:
            return cls(name=row[1], category=row[2], id=row[0])
        return None

    def articles(self):
        CURSOR.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        return CURSOR.fetchall()

    def contributors(self):
        CURSOR.execute('''
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        return CURSOR.fetchall()
