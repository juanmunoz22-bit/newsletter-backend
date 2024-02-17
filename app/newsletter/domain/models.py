from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.newsletter.domain.base import Base


class Campaign(Base):
    __tablename__ = 'campaigns'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255))
    description = Column(String(255))
    category = Column(String(255))
    subject = Column(String(255))
    html_content = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Recipient(Base):
    __tablename__ = 'recipients'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), primary_key=True, unique=True, index=True)
    subscribed = Column(Boolean, default=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class CampaignRecipient(Base):
    __tablename__ = 'campaign_recipients'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email_campaign_id = Column(UUID(as_uuid=True), ForeignKey('campaigns.id'), unique=True)
    recipient_email = Column(String(255), ForeignKey('recipients.email'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)