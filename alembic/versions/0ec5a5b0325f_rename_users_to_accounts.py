"""rename users to accounts

Revision ID: 0ec5a5b0325f
Revises: ee0519d625b9
Create Date: 2024-01-16 22:20:22.934915

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '0ec5a5b0325f'
down_revision: Union[str, None] = 'ee0519d625b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.rename_table('users', 'accounts')


def downgrade():
    op.rename_table('accounts', 'users')
