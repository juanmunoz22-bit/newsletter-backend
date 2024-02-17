from flask import Flask
from flask_cors import CORS

from app.newsletter.routes.routes import newsletter_bp

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

app.register_blueprint(newsletter_bp, url_prefix="/api/v1/newsletter")