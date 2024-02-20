from flask import Flask
from flask_cors import CORS

from app.extensions.celery import celery
from app.extensions.mail import mail
from app.newsletter.routes.routes import newsletter_bp
from app.newsletter.infrastructure.redis.celery import init_celery

def create_app():
    app = Flask(__name__)
    CORS(app, origins="http://localhost:5173")

    app.config['MAIL_SERVER']='smtp-relay.brevo.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'juan.pablo982206@gmail.com'
    app.config['MAIL_PASSWORD'] = 'pISs6O5jEaTv3QmW'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = False
    app.config['SECRET_KEY'] = 'not_a_secret'
    app.config['TESTING'] = False
    app.config['MAIL_DEBUG'] = True
    
    init_celery(app, celery)
    mail.init_app(app)

    app.register_blueprint(newsletter_bp, url_prefix="/api/v1/newsletter")

    return app