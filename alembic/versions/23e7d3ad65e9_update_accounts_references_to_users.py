"""update accounts references to users

Revision ID: 23e7d3ad65e9
Revises: 507452192e5c
Create Date: 2024-01-16 22:41:26.575318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23e7d3ad65e9'
down_revision: Union[str, None] = '507452192e5c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.rename_table('accounts', 'users')


def downgrade():
    op.rename_table('users', 'accounts')
