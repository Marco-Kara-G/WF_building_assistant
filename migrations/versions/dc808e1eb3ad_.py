"""empty message

Revision ID: dc808e1eb3ad
Revises: e4d62207685b
Create Date: 2025-10-22 11:03:57.586631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc808e1eb3ad'
down_revision: Union[str, Sequence[str], None] = 'e4d62207685b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
