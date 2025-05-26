# lib/db/connection.py

import sqlite3

CONN = sqlite3.connect('articles.db')
CURSOR = CONN.cursor()
