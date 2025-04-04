from flask import Flask, render_template
from routes.scraped_routes import scraped_bp
from routes.api_routes import api_bp

app = Flask(__name__, template_folder="templates", static_folder="static")

# Register routes
app.register_blueprint(scraped_bp)
app.register_blueprint(api_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
