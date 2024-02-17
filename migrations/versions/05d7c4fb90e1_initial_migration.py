"""initial migration

Revision ID: 05d7c4fb90e1
Revises: 
Create Date: 2024-02-17 01:43:09.292692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05d7c4fb90e1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('campaigns',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('subject', sa.String(length=255), nullable=True),
    sa.Column('html_content', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipients',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('subscribed', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'email')
    )
    op.create_index(op.f('ix_recipients_email'), 'recipients', ['email'], unique=True)
    op.create_table('campaign_recipients',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('email_campaign_id', sa.UUID(), nullable=True),
    sa.Column('recipient_email', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['email_campaign_id'], ['campaigns.id'], ),
    sa.ForeignKeyConstraint(['recipient_email'], ['recipients.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_campaign_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('campaign_recipients')
    op.drop_index(op.f('ix_recipients_email'), table_name='recipients')
    op.drop_table('recipients')
    op.drop_table('campaigns')
    # ### end Alembic commands ###
