from flask_mail import Mail, Message
from app.extensions.celery import celery as celery_app

@celery_app.task
def send_email(recipient_email, subject, html_content) -> None:
    from app.settings import create_app
    app = create_app()
    with app.app_context():
        mail = Mail(app)    
        msg = Message(
            subject=subject,
            sender="jpmunoz@unbosque.edu.co",
            recipients=[recipient_email],
            html=html_content
        )
        mail.send(msg)