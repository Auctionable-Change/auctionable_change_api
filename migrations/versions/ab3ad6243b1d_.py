"""empty message

Revision ID: ab3ad6243b1d
Revises: c278fa71221a
Create Date: 2020-08-05 17:44:46.872481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab3ad6243b1d'
down_revision = 'c278fa71221a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('charity_score', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'charity_score')
    # ### end Alembic commands ###
