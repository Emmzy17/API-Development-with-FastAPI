"""add foreign-key to posts

Revision ID: 0e6b20f71639
Revises: ee957203abaf
Create Date: 2022-09-04 20:01:07.257193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e6b20f71639'
down_revision = 'ee957203abaf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('')
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
                            local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE"
    )


def downgrade():
    op.drop_constraint("post_users_fk", table_name='posts')
    op.drop_column('posts', 'owner_id')