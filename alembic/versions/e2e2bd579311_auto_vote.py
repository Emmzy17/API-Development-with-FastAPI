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
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes', 
            sa.Column('user_id', sa.Integer(), nullable = False),
            sa.Column('post_id', sa.Integer(), nullable = False), 
            sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete="CASCADE"),
            sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete="CASCADE"),
            sa.PrimaryKeyConstraint('user_id', 'post_id')
            )

    #op.create_foreign_key(None, 'votes', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    #op.create_foreign_key(None, 'votes', 'posts', ['post_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    #op.drop_constraint(None, 'votes', type_='foreignkey')
    #op.drop_constraint(None, 'votes', type_='foreignkey')
    # ### end Alembic commands ###
