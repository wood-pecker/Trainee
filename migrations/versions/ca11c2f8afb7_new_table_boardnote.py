"""New table BoardNote

Revision ID: ca11c2f8afb7
Revises: ba8ce4c74297
Create Date: 2023-11-23 20:36:53.407887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca11c2f8afb7'
down_revision: Union[str, None] = 'ba8ce4c74297'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###