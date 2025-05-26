create_tables()

# Add new author
cristina = Author(name="Cristina")
cristina.save()

# Add new magazine
mag = Magazine(name="Tech Daily", category="Tech")
mag.save()

# Add article
article = Article(title="Intro to ORM", content="Learning is fun", author_id=cristina.id, magazine_id=mag.id)
article.save()

# Fetch articles by Cristina
print(cristina.articles())

# Fetch contributors for Tech Daily
print(get_contributors(mag.id))
