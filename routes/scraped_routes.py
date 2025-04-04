from flask import Blueprint, render_template
import sqlite3

scraped_bp = Blueprint('scraped', __name__)

@scraped_bp.route("/scraped")
def show_scraped_movies():
    conn = sqlite3.connect("db/movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, rating, year, poster_url FROM scraped_movies")
    movies = cursor.fetchall()
    conn.close()
    return render_template("scraped.html", scraped_movies=movies)