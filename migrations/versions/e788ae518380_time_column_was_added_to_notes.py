"""Time column was added to Notes

Revision ID: e788ae518380
Revises: 1a97d03aa44b
Create Date: 2023-11-21 11:49:07.371392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e788ae518380'
down_revision: Union[str, None] = '1a97d03aa44b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('notes', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    op.drop_column('notes', 'time_updated')
    op.drop_column('notes', 'time_created')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('time_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True))
    op.add_column('notes', sa.Column('time_updated', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.drop_column('notes', 'updated_at')
    op.drop_column('notes', 'created_at')
    # ### end Alembic commands ###
