"""update accounts references to users 2

Revision ID: f1dfd621e3d0
Revises: 23e7d3ad65e9
Create Date: 2024-01-16 22:46:16.379615

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1dfd621e3d0'
down_revision: Union[str, None] = '23e7d3ad65e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('messages') as batch_op:
        batch_op.drop_column('recipient')
        batch_op.drop_column('sender')
        batch_op.add_column(sa.Column('recipient', sa.Integer, sa.ForeignKey('users.id')))
        batch_op.add_column(sa.Column('sender', sa.Integer, sa.ForeignKey('users.id')))

    with op.batch_alter_table('peers') as batch_op:
        batch_op.drop_column('user_id')
        batch_op.drop_column('peer_id')
        batch_op.add_column(sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')))
        batch_op.add_column(sa.Column('peer_id', sa.Integer, sa.ForeignKey('users.id')))

    with op.batch_alter_table('user_tags') as batch_op:
        batch_op.drop_column('user_id')
        batch_op.add_column(sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False))


def downgrade():
    with op.batch_alter_table('messages') as batch_op:
        batch_op.drop_column('recipient')
        batch_op.drop_column('sender')
        batch_op.add_column(sa.Column('recipient', sa.Integer, sa.ForeignKey('accounts.id')))
        batch_op.add_column(sa.Column('sender', sa.Integer, sa.ForeignKey('accounts.id')))

    with op.batch_alter_table('peers') as batch_op:
        batch_op.drop_column('user_id')
        batch_op.drop_column('peer_id')
        batch_op.add_column(sa.Column('user_id', sa.Integer, sa.ForeignKey('accounts.id')))
        batch_op.add_column(sa.Column('peer_id', sa.Integer, sa.ForeignKey('accounts.id')))

    with op.batch_alter_table('user_tags') as batch_op:
        batch_op.drop_column('user_id')
        batch_op.add_column(sa.Column('user_id', sa.Integer, sa.ForeignKey('accounts.id'), nullable=False))
