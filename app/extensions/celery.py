from celery import Celery

celery = Celery("app", broker="redis://broker:6379/0", backend="redis://broker:6379/1")

celery.autodiscover_tasks(["app.newsletter.application", "app.newsletter.infrastructure.redis", "app.newsletter.utils.celery.send_email"])