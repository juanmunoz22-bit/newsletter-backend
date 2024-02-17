from celery import Celery

celery = Celery(__name__, broker="redis://localhost:6379/0", backend="redis://localhost:6379/1")

celery.autodiscover_tasks(["app.newsletter.application", "app.newsletter.infrastructure.redis"])