from __future__ import annotations

from pathlib import Path

from flask import Flask, send_from_directory
from flask_cors import CORS

from api import api_bp
from auth import auth_bp
from dotenv import load_dotenv
import os


load_dotenv()
port = os.getenv("FLASK_PORT")  
host = os.getenv("FLASK_HOST") 
debug = os.getenv("FLASK_DEBUG") == "True"

BASE_DIR = Path(__file__).resolve().parents[1]
FRONTEND_DIR = BASE_DIR / "frontend"


def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.get("/")
    def serve_index():
        return send_from_directory(FRONTEND_DIR, "index.html")

    @app.get("/styles.css")
    def serve_styles():
        return send_from_directory(FRONTEND_DIR, "styles.css")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=os.getenv("FLASK_PORT"), debug=True)

