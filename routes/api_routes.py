from flask import Blueprint, render_template
import sqlite3

api_bp = Blueprint('api', __name__)

@api_bp.route("/api")
def show_api_movies():
    conn = sqlite3.connect("db/movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, plot, poster_url FROM api_movies")
    movies = cursor.fetchall()
    conn.close()
    return render_template("api.html", api_movies=movies)
