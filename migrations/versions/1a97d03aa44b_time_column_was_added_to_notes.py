"""Time column was added to Notes

Revision ID: 1a97d03aa44b
Revises: c342c5ccd57a
Create Date: 2023-11-21 11:46:57.538308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a97d03aa44b'
down_revision: Union[str, None] = 'c342c5ccd57a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('notes', sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True))
    op.add_column('notes', sa.Column('views_amount', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('notes', 'views_amount')
    op.drop_column('notes', 'time_updated')
    op.drop_column('notes', 'time_created')
    # ### end Alembic commands ###
