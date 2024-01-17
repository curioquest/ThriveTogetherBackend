"""update accounts references

Revision ID: 507452192e5c
Revises: 0ec5a5b0325f
Create Date: 2024-01-16 22:26:39.241699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '507452192e5c'
down_revision: Union[str, None] = '0ec5a5b0325f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
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


def downgrade():
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
