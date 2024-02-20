from app.settings import create_app
from app.extensions.celery import celery
from app.newsletter.infrastructure.redis.celery import init_celery

if __name__ == "__main__":
    app = create_app()
    celery = init_celery(app, celery)
    app.run(debug=True)
