import sqlite3

connection = sqlite3.connect('db/articles.db')
cursor = connection.cursor()

# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS authors")
cursor.execute("DROP TABLE IF EXISTS magazines")
cursor.execute("DROP TABLE IF EXISTS articles")

# Create tables
cursor.execute("""
    CREATE TABLE authors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        genre TEXT
    )
""")

cursor.execute("""
    CREATE TABLE magazines (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT
    )
""")

cursor.execute("""
    CREATE TABLE articles (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        content TEXT,
        author_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id)
    )
""")

# Seed data (optional)
cursor.execute("INSERT INTO authors (name, genre) VALUES ('Cristina', 'Tech')")
cursor.execute("INSERT INTO magazines (name, category) VALUES ('Code Weekly', 'Technology')")
cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES ('Intro to Python', 'Learn Python basics...', 1, 1)")

connection.commit()
connection.close()
