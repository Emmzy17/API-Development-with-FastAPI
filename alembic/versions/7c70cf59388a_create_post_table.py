"""create post table

Revision ID: 7c70cf59388a
Revises: 
Create Date: 2022-09-04 19:13:02.847238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c70cf59388a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key = True), 
    sa.Column('title', sa.String(), nullable=False,  ))


def downgrade():
    op.drop_table('posts')
