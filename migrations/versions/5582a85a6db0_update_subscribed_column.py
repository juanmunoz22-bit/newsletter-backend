"""update subscribed column

Revision ID: 5582a85a6db0
Revises: e62b77a94586
Create Date: 2024-02-20 00:33:21.521818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5582a85a6db0'
down_revision: Union[str, None] = 'e62b77a94586'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('campaign_recipients', 'subscribed')
    op.add_column('recipients', sa.Column('subscribed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipients', 'subscribed')
    op.add_column('campaign_recipients', sa.Column('subscribed', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###