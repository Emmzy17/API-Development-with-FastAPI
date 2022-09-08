"""add last columns of post

Revision ID: be2316e2c935
Revises: 0e6b20f71639
Create Date: 2022-09-05 21:38:56.006434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be2316e2c935'
down_revision = '0e6b20f71639'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default ='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default = sa.text('NOW()')))


def downgrade():
    pass
