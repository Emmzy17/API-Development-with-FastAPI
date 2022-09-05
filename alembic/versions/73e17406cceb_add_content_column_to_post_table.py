"""add content column to post table

Revision ID: 73e17406cceb
Revises: 7c70cf59388a
Create Date: 2022-09-04 19:38:15.511713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73e17406cceb'
down_revision = '7c70cf59388a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))

def downgrade():
    op.drop_column('posts', 'content')
