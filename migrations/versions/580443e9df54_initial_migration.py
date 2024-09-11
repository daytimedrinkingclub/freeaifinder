"""Initial Migration

Revision ID: 580443e9df54
Revises: 
Create Date: 2024-09-11 08:37:36.006884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '580443e9df54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('pros', sa.Text(), nullable=True),
    sa.Column('cons', sa.Text(), nullable=True),
    sa.Column('website', sa.String(length=200), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tool_submission',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('website', sa.String(length=200), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tool_submission')
    op.drop_table('tool')
    # ### end Alembic commands ###
