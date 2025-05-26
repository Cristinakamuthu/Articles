# lib/debug.py

from lib.author import Author

if __name__ == "__main__":
    # Create author and save to DB for testing
    author = Author("Cristina the Coder 🧠💅")
    author.save()
    print("Author saved to DB!")
