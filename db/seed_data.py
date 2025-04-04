import sqlite3
import os

DB_PATH = "db/movies.db"
if not os.path.exists("db"):
    os.makedirs("db")

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS scraped_movies")
c.execute("CREATE TABLE scraped_movies (id INTEGER PRIMARY KEY, title TEXT, rating TEXT, year TEXT, poster_url TEXT)")
c.execute("INSERT INTO scraped_movies (title, rating, year, poster_url) VALUES (?, ?, ?, ?)",
          ("The Shawshank Redemption", "9.3", "1994", "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg"))

c.execute("DROP TABLE IF EXISTS api_movies")
c.execute("CREATE TABLE api_movies (id INTEGER PRIMARY KEY, title TEXT, genre TEXT, plot TEXT, poster_url TEXT)")
c.execute("INSERT INTO api_movies (title, genre, plot, poster_url) VALUES (?, ?, ?, ?)",
          ("Inception", "Action, Sci-Fi", "A thief who steals corporate secrets through dream-sharing.",
           "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg"))

conn.commit()
conn.close()
