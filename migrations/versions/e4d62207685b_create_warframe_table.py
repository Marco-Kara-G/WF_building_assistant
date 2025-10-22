"""create warframe table

Revision ID: e4d62207685b
Revises: f158d7e5932e
Create Date: 2025-10-22 10:58:40.778256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4d62207685b'
down_revision: Union[str, Sequence[str], None] = 'f158d7e5932e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
