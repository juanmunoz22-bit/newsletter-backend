from typing import List

from app.newsletter.domain.models import Campaign, Recipient, CampaignRecipient
from app.newsletter.infrastructure.postgres.repository import EmailRepository
from app.newsletter.infrastructure.redis.celery import celery

class EmailService:
    @staticmethod
    def send_campaign(email_campaign_id):
        campaign = EmailRepository.get_campaign(email_campaign_id)
        recipients: List[Recipient] = campaign.recipients
        for recipient in recipients:
            send_email.delay(recipient.email, campaign.subject, campaign.html_content)

    @staticmethod
    def create_campaign(name, description, category, subject, html_content):
        campaign = Campaign(name=name, description=description, category=category, subject=subject, html_content=html_content)
        EmailRepository.save_campaign(campaign)
        return campaign

    @staticmethod
    def create_recipients(emails):
        recipients_tuple = EmailRepository.get_recipients_emails()
        recipients = [recipient[0] for recipient in recipients_tuple]
        new_emails = [email for email in emails if email not in recipients]
        new_recipients = [Recipient(email=email) for email in new_emails]
        EmailRepository.save_recipients(new_recipients)

    @staticmethod
    def add_recipient_to_campaign(email_campaign_id, recipient_emails):
        campaign_recipients = [
            CampaignRecipient(email_campaign_id=email_campaign_id, recipient_email=recipient_email)
            for recipient_email in recipient_emails
        ]
        EmailRepository.save_campaign_recipients(campaign_recipients)

@celery.task
def send_email(recipient_email, subject, html_content) -> None:
    pass