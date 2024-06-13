"""add user

Revision ID: 72f6959a1407
Revises: 59140b7ce59e
Create Date: 2024-06-12 23:25:10.081879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '72f6959a1407'
down_revision: Union[str, None] = '59140b7ce59e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('notes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'notes', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notes', type_='foreignkey')
    op.drop_column('notes', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###