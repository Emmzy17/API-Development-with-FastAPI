"""auto-vote

Revision ID: e2e2bd579311
Revises: be2316e2c935
Create Date: 2022-09-06 21:36:00.338055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2e2bd579311'
down_revision = 'be2316e2c935'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('votes', 
            sa.Column('user_id', sa.Integer(), nullable=False),
            sa.Column('post_id', sa.Integer(), nullable=False), 
            sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
            sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
            sa.PrimaryKeyConstraint('user_id', 'post_id'),
            )

  

def downgrade():
    
    op.drop_table('votes')
    