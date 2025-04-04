CREATE TABLE scraped_movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    rating TEXT,
    year TEXT,
    poster_url TEXT
);

CREATE TABLE api_movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    plot TEXT,
    poster_url TEXT
);