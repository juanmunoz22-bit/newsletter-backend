from typing import List
from app.newsletter.domain.models import Campaign, Recipient, CampaignRecipient
from app.newsletter.infrastructure.postgres.database import db_session


class EmailRepository:
    @classmethod
    def get_campaign(cls, email_campaign_id):
        return db_session.query(Campaign).filter(Campaign.id == email_campaign_id).first()

    @classmethod
    def save_campaign(cls, campaign: Campaign) -> None:
        db_session.add(campaign)
        db_session.commit()
        db_session.refresh(campaign)
        return campaign

    @classmethod
    def save_recipients(cls, recipients: List[Recipient]) -> None:
        db_session.bulk_save_objects(recipients)
        db_session.commit()

    @classmethod
    def save_campaign_recipients(cls, campaign_recipients: list) -> None:
        db_session.bulk_save_objects(campaign_recipients)
        db_session.commit()

    @classmethod
    def get_recipient(cls, email):
        return db_session.query(Recipient).filter(Recipient.email == email).first()

    @classmethod
    def get_recipients_emails(cls):
        return db_session.query(Recipient.email).all()

    @classmethod
    def get_campaigns(cls):
        return db_session.query(Campaign).all()

    @classmethod
    def get_campaign_recipients(cls, email_campaign_id):
        result = db_session.query(CampaignRecipient.recipient_email).filter(
            CampaignRecipient.email_campaign_id == email_campaign_id).all()
        return [email[0] for email in result]
    
    @classmethod
    def update_subscription(cls, email):
        recipient = cls.get_recipient(email)
        recipient.subscribed = False
        db_session.commit()
        return recipient