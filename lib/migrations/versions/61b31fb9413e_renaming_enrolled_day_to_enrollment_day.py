"""Renaming enrolled_day to enrollment_day



Revision ID: 61b31fb9413e
Revises: 791279dd0760
Create Date: 2024-03-31 17:45:17.176630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61b31fb9413e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'enrolled-day', enrollment_day='Column(DateTime(), default=datetime.now())')


def downgrade() -> None:
    op.alter_column('students', 'enrollment_day', enrolled_day='enrolled_day')
