from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Seed authors
    authors = ['Alice Walker', 'John Steinbeck', 'Toni Morrison']
    for name in authors:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))

    # Seed magazines
    magazines = [('Time', 'News'), ('Vogue', 'Fashion'), ('Scientific American', 'Science')]
    for name, category in magazines:
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))

    # Seed articles (now with content!)
    articles = [
        ('The Color Purple Review', 'A deep dive into Alice Walker’s masterpiece.', 1, 1),
        ('East of Eden Analysis', 'Exploring the moral philosophy in Steinbeck’s classic.', 2, 2),
        ('Beloved Breakdown', 'Themes of memory and trauma in Morrison’s Beloved.', 3, 3)
    ]
    for title, content, author_id, magazine_id in articles:
        cursor.execute(
            "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
            (title, content, author_id, magazine_id)
        )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_data()
    print("Database seeded successfully!")
